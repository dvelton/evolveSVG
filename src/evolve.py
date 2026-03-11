"""
evolve.py — Main orchestration script for the self-evolving SVG generator.
Loads the current generator, mutates it, scores variants, selects the winner,
and updates all project files (history, lineage, README, hall of fame, etc).
"""
import ast
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
from datetime import datetime, timezone
from pathlib import Path

# Resolve paths relative to the repo root (parent of src/)
REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
OUTPUT_DIR = REPO_ROOT / "output"
GRAVEYARD_DIR = REPO_ROOT / "graveyard"
HOF_DIR = OUTPUT_DIR / "hall_of_fame"
SNAPSHOTS_DIR = OUTPUT_DIR / "snapshots"
GENERATOR_PATH = SRC_DIR / "generator.py"
HISTORY_PATH = OUTPUT_DIR / "history.json"
CURRENT_SVG = OUTPUT_DIR / "current.svg"
SPARKLINE_SVG = OUTPUT_DIR / "fitness_history.svg"
EVOLUTION_HTML = OUTPUT_DIR / "evolution.html"
LINEAGE_PATH = REPO_ROOT / "LINEAGE.md"
README_PATH = REPO_ROOT / "README.md"

# Add src to path so we can import siblings
sys.path.insert(0, str(SRC_DIR))
import mutator
import fitness


def load_history() -> dict:
    """Load or initialize the evolution history."""
    if HISTORY_PATH.exists():
        with open(HISTORY_PATH, "r") as f:
            return json.load(f)
    return {"generation": 0, "entries": [], "genome": "", "past_svgs": []}


def save_history(history: dict):
    """Persist the evolution history."""
    with open(HISTORY_PATH, "w") as f:
        json.dump(history, f, indent=2)


def run_generator(source: str) -> str:
    """Execute a generator source and capture its SVG output."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
        tmp.write(source)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            [sys.executable, tmp_path],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            return ""
        return result.stdout.strip()
    except (subprocess.TimeoutExpired, Exception):
        return ""
    finally:
        os.unlink(tmp_path)


def count_ast_nodes(source: str) -> int:
    """Count AST nodes in source code for complexity tracking."""
    try:
        tree = ast.parse(source)
        return sum(1 for _ in ast.walk(tree))
    except SyntaxError:
        return 0


def detect_plateau(history: dict) -> bool:
    """Check if fitness has plateaued over the last 10 generations."""
    entries = history.get("entries", [])
    if len(entries) < 10:
        return False

    recent = entries[-10:]
    scores = [e["fitness"] for e in recent]
    if scores[0] == 0:
        return False

    improvement = (scores[-1] - scores[0]) / max(abs(scores[0]), 0.01)
    return improvement < 0.02


def generate_sparkline(history: dict):
    """Generate an SVG sparkline of fitness history."""
    entries = history.get("entries", [])
    if len(entries) < 2:
        # Minimal placeholder
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="400" height="60">'
               '<text x="10" y="35" fill="#888" font-size="12">'
               'Fitness history will appear after generation 1</text></svg>')
        with open(SPARKLINE_SVG, "w") as f:
            f.write(svg)
        return

    # Use last 50 entries
    recent = entries[-50:]
    scores = [e["fitness"] for e in recent]
    min_s = min(scores)
    max_s = max(scores)
    spread = max_s - min_s if max_s != min_s else 1.0

    w, h = 400, 60
    padding = 5
    plot_w = w - 2 * padding
    plot_h = h - 2 * padding

    points = []
    for i, s in enumerate(scores):
        x = padding + (i / max(len(scores) - 1, 1)) * plot_w
        y = padding + plot_h - ((s - min_s) / spread) * plot_h
        points.append(f"{x:.1f},{y:.1f}")

    polyline = " ".join(points)
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">',
        f'<rect width="{w}" height="{h}" fill="#0d1117" rx="4"/>',
        f'<polyline points="{polyline}" fill="none" stroke="#58a6ff" stroke-width="1.5"/>',
    ]

    # Dot on the latest point
    last = points[-1]
    svg_parts.append(f'<circle cx="{last.split(",")[0]}" cy="{last.split(",")[1]}" '
                     f'r="2.5" fill="#58a6ff"/>')
    svg_parts.append('</svg>')

    with open(SPARKLINE_SVG, "w") as f:
        f.write("\n".join(svg_parts))


def update_hall_of_fame(history: dict, source: str, svg_content: str,
                        gen: int, score_val: float):
    """Maintain the top 5 all-time generators."""
    HOF_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = HOF_DIR / "manifest.json"

    if manifest_path.exists():
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
    else:
        manifest = []

    entry = {"generation": gen, "fitness": score_val}

    # Check if this belongs in top 5
    manifest.append(entry)
    manifest.sort(key=lambda e: e["fitness"], reverse=True)
    manifest = manifest[:5]

    # Only keep files for entries in the manifest
    keep_gens = {e["generation"] for e in manifest}

    if gen in keep_gens:
        with open(HOF_DIR / f"gen_{gen}.py", "w") as f:
            f.write(source)
        with open(HOF_DIR / f"gen_{gen}.svg", "w") as f:
            f.write(svg_content)

    # Clean up any files not in the current top 5
    for path in HOF_DIR.glob("gen_*.py"):
        g = int(path.stem.split("_")[1])
        if g not in keep_gens:
            path.unlink()
            svg_path = HOF_DIR / f"gen_{g}.svg"
            if svg_path.exists():
                svg_path.unlink()

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)


def save_snapshot(gen: int, svg_content: str):
    """Save a generation snapshot every 10 generations."""
    SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(SNAPSHOTS_DIR / f"gen_{gen}.svg", "w") as f:
        f.write(svg_content)


def update_lineage(history: dict):
    """Regenerate LINEAGE.md from history."""
    entries = history.get("entries", [])

    lines = [
        "# Lineage",
        "",
        "Evolution history of the SVG generator. Each entry records a generation,",
        "what mutation was applied, and how fitness changed.",
        "",
        "---",
        "",
    ]

    for entry in reversed(entries):
        gen = entry["generation"]
        mut = entry["mutation_type"]
        fit = entry["fitness"]
        delta = entry.get("delta", 0)
        desc = entry.get("description", "")
        extinction = entry.get("extinction", False)

        delta_str = f"+{delta:.2f}" if delta >= 0 else f"{delta:.2f}"
        prefix = "EXTINCTION " if extinction else ""

        lines.append(f"### {prefix}Generation {gen}")
        lines.append(f"**Mutation:** {mut} | **Fitness:** {fit:.2f} ({delta_str}) | {desc}")

        # Embed snapshot image every 10 generations
        snapshot = SNAPSHOTS_DIR / f"gen_{gen}.svg"
        if snapshot.exists():
            lines.append("")
            lines.append(f"![gen {gen}](output/snapshots/gen_{gen}.svg)")

        lines.append("")

    with open(LINEAGE_PATH, "w") as f:
        f.write("\n".join(lines))


def mutation_description(mutation_type: str, is_extinction: bool) -> str:
    """Generate a one-line description of the mutation."""
    descriptions = {
        "numeric_drift": "Adjusted numeric parameters",
        "structural_swap": "Swapped shape drawing blocks",
        "color_shift": "Shifted color palette",
        "additive": "Added duplicated shape elements",
        "none": "No effective mutation",
    }
    base = descriptions.get(mutation_type, "Applied mutation")
    if is_extinction:
        base = "EXTINCTION EVENT: " + base + " (triple mutation, 8 variants)"
    return base


def update_readme(history: dict):
    """Regenerate README.md with current stats."""
    gen = history.get("generation", 0)
    genome = history.get("genome", "")
    entries = history.get("entries", [])
    current_fitness = entries[-1]["fitness"] if entries else 0

    fitness_str = f"{current_fitness:.2f}"

    lines = [
        "# evolveSVG",
        "",
        "A self-evolving repository. The code in this repo mutates itself on a schedule,",
        "generating new SVG artwork through genetic programming. No human writes code after",
        "the initial commit. The git history is a fossil record of artificial evolution.",
        "",
        f"![generation](https://img.shields.io/badge/generation-{gen}-blue)"
        f" ![fitness](https://img.shields.io/badge/fitness-{fitness_str}-brightgreen)",
        "",
        "## Current Output",
        "",
        "![current evolution](output/current.svg)",
        "",
        "## Fitness Over Time",
        "",
        "![fitness sparkline](output/fitness_history.svg)",
        "",
        "## Mutation Genome",
        "",
        "Each character represents one generation's mutation type:",
        "`N`=numeric drift, `S`=structural swap, `C`=color shift, "
        "`A`=additive, `E`=extinction event",
        "",
        f"```",
        f"{genome if genome else '(empty — generation 0)'}",
        f"```",
        "",
        "## How It Works",
        "",
        "1. A GitHub Actions cron job runs 10 times per day",
        "2. The `mutator` parses `generator.py` using Python's `ast` module "
        "and applies random mutations",
        "3. Four mutant variants are generated and executed",
        "4. Each variant's SVG output is scored on complexity, spatial distribution, "
        "color diversity, and novelty",
        "5. The highest-scoring variant becomes the new `generator.py`",
        "6. Losers are archived in the `graveyard/`",
        "7. If fitness plateaus for 10 generations, an extinction event triggers "
        "triple mutations with 8 variants",
        "",
        "Zero external dependencies. Pure Python stdlib. No API calls. "
        "The only input is the repo's own past.",
        "",
        "## Links",
        "",
        "- [Lineage](LINEAGE.md) — full evolution history with visual snapshots",
        "- [Hall of Fame](output/hall_of_fame/) — top 5 all-time generators",
        "- [Evolution Animation](output/evolution.html) — animated playback "
        "(clone and open locally)",
        "- [Graveyard](graveyard/) — every losing variant, preserved for the record",
    ]

    with open(README_PATH, "w") as f:
        f.write("\n".join(lines))


def update_evolution_html():
    """Generate an HTML page that animates through recent SVG snapshots."""
    snapshots = sorted(SNAPSHOTS_DIR.glob("gen_*.svg"),
                       key=lambda p: int(p.stem.split("_")[1]))
    # Keep last 20
    snapshots = snapshots[-20:]

    if not snapshots:
        return

    svg_data = []
    for snap in snapshots:
        gen_num = snap.stem.split("_")[1]
        content = snap.read_text()
        # Escape for JS embedding
        escaped = content.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
        svg_data.append(f'  {{gen: {gen_num}, svg: `{escaped}`}}')

    frames_js = ",\n".join(svg_data)

    html = textwrap.dedent(f"""\
    <!DOCTYPE html>
    <html>
    <head>
      <title>evolveSVG — Evolution Animation</title>
      <style>
        body {{
          background: #0d1117;
          color: #c9d1d9;
          font-family: monospace;
          display: flex;
          flex-direction: column;
          align-items: center;
          padding: 20px;
        }}
        #display {{ margin: 20px 0; }}
        #info {{ font-size: 14px; margin: 10px 0; }}
        button {{
          background: #21262d;
          color: #c9d1d9;
          border: 1px solid #30363d;
          padding: 8px 16px;
          cursor: pointer;
          margin: 0 4px;
          font-family: monospace;
        }}
        button:hover {{ background: #30363d; }}
      </style>
    </head>
    <body>
      <h1>evolveSVG Evolution</h1>
      <div id="info">Loading...</div>
      <div id="display"></div>
      <div>
        <button onclick="togglePlay()">Play/Pause</button>
        <button onclick="step(-1)">Prev</button>
        <button onclick="step(1)">Next</button>
      </div>
      <script>
        const frames = [
    {frames_js}
        ];
        let idx = 0;
        let playing = true;
        const display = document.getElementById('display');
        const info = document.getElementById('info');
        function show() {{
          if (!frames.length) return;
          display.innerHTML = frames[idx].svg;
          info.textContent = 'Generation ' + frames[idx].gen +
            ' (' + (idx+1) + '/' + frames.length + ')';
        }}
        function step(d) {{
          idx = (idx + d + frames.length) % frames.length;
          show();
        }}
        function togglePlay() {{ playing = !playing; }}
        show();
        setInterval(() => {{ if (playing) step(1); }}, 1000);
      </script>
    </body>
    </html>
    """)

    with open(EVOLUTION_HTML, "w") as f:
        f.write(html)


def main():
    # Ensure directories exist
    for d in [OUTPUT_DIR, GRAVEYARD_DIR, HOF_DIR, SNAPSHOTS_DIR]:
        d.mkdir(parents=True, exist_ok=True)

    # Load state
    history = load_history()
    gen = history["generation"]
    past_svgs = history.get("past_svgs", [])

    # Load current generator source
    source = GENERATOR_PATH.read_text()

    # Run current generator to establish baseline
    baseline_svg = run_generator(source)
    if not baseline_svg:
        print("ERROR: Current generator failed to produce output. Aborting.")
        sys.exit(1)

    baseline_score = fitness.score(baseline_svg, past_svgs)

    # Check for extinction event
    is_extinction = detect_plateau(history)
    num_variants = 8 if is_extinction else 4

    if is_extinction:
        print(f"EXTINCTION EVENT at generation {gen + 1}")
        # Triple mutation: apply 3 rounds
        variants = []
        for _ in range(num_variants):
            mutated = source
            applied_types = []
            for _round in range(3):
                results = mutator.mutate(mutated, num_variants=1)
                mutated = results[0][0]
                applied_types.append(results[0][1])
            variants.append((mutated, "extinction"))
        mutation_type = "extinction"
    else:
        # Normal mutation
        variants = mutator.mutate(source, num_variants=num_variants)
        mutation_type = variants[0][1] if variants else "none"

    # Run and score all variants
    scored = []
    for i, (variant_source, mut_type) in enumerate(variants):
        svg_output = run_generator(variant_source)
        if not svg_output:
            continue
        s = fitness.score(svg_output, past_svgs)
        scored.append({
            "index": i,
            "source": variant_source,
            "svg": svg_output,
            "score": s,
            "mutation_type": mut_type,
        })

    if not scored:
        print("All variants failed. Keeping current generator.")
        return

    # Also include the baseline as a candidate (ensures we never regress)
    scored.append({
        "index": -1,
        "source": source,
        "svg": baseline_svg,
        "score": baseline_score,
        "mutation_type": "baseline",
    })

    # Select winner
    scored.sort(key=lambda x: x["score"], reverse=True)
    winner = scored[0]
    losers = [s for s in scored[1:] if s["index"] != -1]

    new_gen = gen + 1
    delta = winner["score"] - baseline_score

    print(f"Generation {new_gen}: {mutation_type} | "
          f"fitness {winner['score']:.2f} (delta {delta:+.2f})")

    # Write winner
    GENERATOR_PATH.write_text(winner["source"])
    with open(CURRENT_SVG, "w") as f:
        f.write(winner["svg"])

    # Save losers to graveyard
    for loser in losers:
        loser_path = GRAVEYARD_DIR / f"gen_{new_gen}_loser_{loser['index']}.py"
        with open(loser_path, "w") as f:
            f.write(loser["source"])

    # Update past SVGs (keep last 5)
    past_svgs.append(winner["svg"])
    past_svgs = past_svgs[-5:]

    # Genome character
    genome_char = {
        "numeric_drift": "N",
        "structural_swap": "S",
        "color_shift": "C",
        "additive": "A",
        "extinction": "E",
        "none": ".",
        "baseline": ".",
    }.get(winner["mutation_type"], "?")

    # Build history entry
    entry = {
        "generation": new_gen,
        "mutation_type": mutation_type,
        "fitness": winner["score"],
        "delta": round(delta, 4),
        "ast_nodes": count_ast_nodes(winner["source"]),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "extinction": is_extinction,
        "description": mutation_description(mutation_type, is_extinction),
    }

    history["generation"] = new_gen
    history["entries"].append(entry)
    history["genome"] = history.get("genome", "") + genome_char
    history["past_svgs"] = past_svgs

    save_history(history)

    # Hall of fame
    update_hall_of_fame(history, winner["source"], winner["svg"],
                        new_gen, winner["score"])

    # Snapshot every 10 generations (and gen 1)
    if new_gen == 1 or new_gen % 10 == 0:
        save_snapshot(new_gen, winner["svg"])

    # Regenerate derived files
    generate_sparkline(history)
    update_lineage(history)
    update_readme(history)
    update_evolution_html()

    print(f"Evolution complete. Generation {new_gen} committed.")


if __name__ == "__main__":
    main()

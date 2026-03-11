"""
mutator.py — AST-level mutation engine for generator.py
Mutation types:
  1. numeric_drift  — small random changes to float/int literals
  2. structural_swap — swap two similar operations
  3. color_shift     — mutate hex color string values
  4. additive        — duplicate and offset a shape block
All mutations are validated with compile(). Falls back to numeric_drift on failure.
"""
import ast
import copy
import random
import re
import textwrap


def mutate(source: str, mutation_type: str = None, num_variants: int = 4) -> list:
    """
    Given the source code of generator.py, produce num_variants mutated versions.
    Returns a list of (mutated_source, mutation_type) tuples.
    """
    if mutation_type is None:
        mutation_type = random.choice(["numeric_drift", "structural_swap",
                                       "color_shift", "additive"])

    variants = []
    for _ in range(num_variants):
        try:
            if mutation_type == "numeric_drift":
                result = _numeric_drift(source)
            elif mutation_type == "structural_swap":
                result = _structural_swap(source)
            elif mutation_type == "color_shift":
                result = _color_shift(source)
            elif mutation_type == "additive":
                result = _additive(source)
            else:
                result = _numeric_drift(source)

            # Validate the result compiles
            compile(result, "<mutant>", "exec")
            variants.append((result, mutation_type))
        except Exception:
            # Fallback to numeric drift
            try:
                result = _numeric_drift(source)
                compile(result, "<mutant>", "exec")
                variants.append((result, "numeric_drift"))
            except Exception:
                # Last resort: return source unchanged
                variants.append((source, "none"))

    return variants


def _numeric_drift(source: str) -> str:
    """Randomly adjust int and float literals by +/- 5-20%."""
    tree = ast.parse(source)
    numerics = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            # Skip 0, 1, 2 (likely structural), and very small values
            if isinstance(node.value, int) and abs(node.value) <= 2:
                continue
            if isinstance(node.value, float) and abs(node.value) < 0.01:
                continue
            numerics.append(node)

    if not numerics:
        return source

    # Mutate 1-3 random numeric literals
    count = random.randint(1, min(3, len(numerics)))
    targets = random.sample(numerics, count)

    for node in targets:
        drift = random.uniform(0.05, 0.20) * random.choice([-1, 1])
        new_val = node.value * (1.0 + drift)
        if isinstance(node.value, int):
            new_val = int(round(new_val))
            if new_val == 0:
                new_val = node.value  # don't zero out
        else:
            new_val = round(new_val, 2)
        node.value = new_val

    return ast.unparse(tree)


def _structural_swap(source: str) -> str:
    """Swap two similar AST statement blocks within the generate_svg function."""
    tree = ast.parse(source)

    # Find the generate_svg function
    func = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "generate_svg":
            func = node
            break

    if func is None:
        return _numeric_drift(source)

    # Find for-loops (shape drawing blocks) to swap
    loops = [stmt for stmt in func.body if isinstance(stmt, ast.For)]

    if len(loops) < 2:
        return _numeric_drift(source)

    # Pick two random loops and swap their bodies
    i, j = random.sample(range(len(loops)), 2)
    loop_indices = []
    for idx, stmt in enumerate(func.body):
        if isinstance(stmt, ast.For):
            loop_indices.append(idx)

    if len(loop_indices) < 2:
        return _numeric_drift(source)

    idx_a = loop_indices[i]
    idx_b = loop_indices[j]
    func.body[idx_a], func.body[idx_b] = func.body[idx_b], func.body[idx_a]
    ast.fix_missing_locations(tree)

    return ast.unparse(tree)


def _color_shift(source: str) -> str:
    """Find hex color strings and shift their RGB channels."""
    hex_pattern = re.compile(r'#([0-9a-fA-F]{6})')

    matches = list(hex_pattern.finditer(source))
    if not matches:
        return _numeric_drift(source)

    # Pick 1-3 colors to mutate
    count = random.randint(1, min(3, len(matches)))
    targets = random.sample(matches, count)

    result = source
    # Process in reverse order to preserve positions
    for match in sorted(targets, key=lambda m: m.start(), reverse=True):
        hex_str = match.group(1)
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)

        # Shift each channel by a random amount
        r = max(0, min(255, r + random.randint(-40, 40)))
        g = max(0, min(255, g + random.randint(-40, 40)))
        b = max(0, min(255, b + random.randint(-40, 40)))

        new_color = f"#{r:02x}{g:02x}{b:02x}"
        result = result[:match.start()] + new_color + result[match.end():]

    # Validate it still compiles
    compile(result, "<mutant>", "exec")
    return result


def _additive(source: str) -> str:
    """Duplicate a shape-drawing block (a for-loop) with offset parameters."""
    tree = ast.parse(source)

    func = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "generate_svg":
            func = node
            break

    if func is None:
        return _numeric_drift(source)

    # Find for-loops to duplicate
    loop_indices = []
    for idx, stmt in enumerate(func.body):
        if isinstance(stmt, ast.For):
            loop_indices.append(idx)

    if not loop_indices:
        return _numeric_drift(source)

    # Pick a random loop to duplicate
    src_idx = random.choice(loop_indices)
    new_loop = copy.deepcopy(func.body[src_idx])

    # Apply numeric drift to the duplicated loop's literals
    _drift_node(new_loop)

    # Insert the duplicated loop right after the original
    # but before the closing </svg> append
    insert_pos = src_idx + 1
    func.body.insert(insert_pos, new_loop)
    ast.fix_missing_locations(tree)

    return ast.unparse(tree)


def _drift_node(node):
    """Apply numeric drift to all numeric literals in an AST node."""
    for child in ast.walk(node):
        if isinstance(child, ast.Constant) and isinstance(child.value, (int, float)):
            if isinstance(child.value, int) and abs(child.value) <= 2:
                continue
            if isinstance(child.value, float) and abs(child.value) < 0.01:
                continue
            drift = random.uniform(0.1, 0.3) * random.choice([-1, 1])
            new_val = child.value * (1.0 + drift)
            if isinstance(child.value, int):
                new_val = int(round(new_val))
                if new_val == 0:
                    new_val = child.value
            else:
                new_val = round(new_val, 2)
            child.value = new_val

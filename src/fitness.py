"""
fitness.py — Scoring function for evolved SVG output.
Scores on four axes (each 0-25, total 0-100):
  1. Visual complexity — count of distinct SVG elements
  2. Spatial distribution — how spread out elements are across the canvas
  3. Color diversity — number of unique colors used
  4. Novelty — how different from recent ancestors (last 5 generations)
Returns a single float. Uses only Python stdlib.
"""
import math
import random
import re
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher


def score(svg_content: str, past_svgs: list = None) -> float:
    """
    Score an SVG string. past_svgs is a list of up to 5 recent SVG strings
    for novelty comparison. Returns a float (higher is better).
    """
    if past_svgs is None:
        past_svgs = []

    complexity = _visual_complexity(svg_content)
    distribution = _spatial_distribution(svg_content)
    colors = _color_diversity(svg_content)
    novelty = _novelty(svg_content, past_svgs)

    total = complexity + distribution + colors + novelty

    # Tiny random tiebreaker to prevent exact ties
    total += random.uniform(0.0001, 0.001)

    return round(total, 4)


def _visual_complexity(svg_content: str) -> float:
    """Score based on count of SVG shape elements. Max 25."""
    try:
        root = ET.fromstring(svg_content)
    except ET.ParseError:
        return 0.0

    shape_tags = {'circle', 'rect', 'line', 'ellipse', 'polygon',
                  'polyline', 'path', 'text'}
    count = 0
    for elem in root.iter():
        tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
        if tag in shape_tags:
            count += 1

    # Scale: 0 elements = 0, 50+ elements = 25
    return min(25.0, (count / 50.0) * 25.0)


def _spatial_distribution(svg_content: str) -> float:
    """Score based on how spread out elements are. Max 25."""
    try:
        root = ET.fromstring(svg_content)
    except ET.ParseError:
        return 0.0

    positions = []
    for elem in root.iter():
        # Collect position attributes
        x = elem.get('cx') or elem.get('x') or elem.get('x1')
        y = elem.get('cy') or elem.get('y') or elem.get('y1')
        if x is not None and y is not None:
            try:
                positions.append((float(x), float(y)))
            except ValueError:
                continue

    if len(positions) < 2:
        return 0.0

    # Calculate variance of positions
    mean_x = sum(p[0] for p in positions) / len(positions)
    mean_y = sum(p[1] for p in positions) / len(positions)
    var_x = sum((p[0] - mean_x) ** 2 for p in positions) / len(positions)
    var_y = sum((p[1] - mean_y) ** 2 for p in positions) / len(positions)
    spread = math.sqrt(var_x + var_y)

    # Scale: 0 spread = 0, 200+ spread = 25
    return min(25.0, (spread / 200.0) * 25.0)


def _color_diversity(svg_content: str) -> float:
    """Score based on number of unique colors. Max 25."""
    hex_colors = set(re.findall(r'#[0-9a-fA-F]{6}', svg_content))
    rgb_colors = set(re.findall(r'rgb\([^)]+\)', svg_content))
    named_colors = set()
    color_attrs = re.findall(r'(?:fill|stroke|color)="([^"#]+)"', svg_content)
    for c in color_attrs:
        c = c.strip()
        if c and c != 'none' and not c.startswith('url'):
            named_colors.add(c)

    total_colors = len(hex_colors) + len(rgb_colors) + len(named_colors)

    # Scale: 0 colors = 0, 20+ colors = 25
    return min(25.0, (total_colors / 20.0) * 25.0)


def _novelty(svg_content: str, past_svgs: list) -> float:
    """Score based on difference from recent ancestors. Max 25."""
    if not past_svgs:
        return 25.0  # First generation is maximally novel

    similarities = []
    for past in past_svgs:
        ratio = SequenceMatcher(None, svg_content, past).ratio()
        similarities.append(ratio)

    # Average similarity to recent ancestors
    avg_similarity = sum(similarities) / len(similarities)
    # Convert to novelty: 0% similar = 25, 100% similar = 0
    novelty = (1.0 - avg_similarity) * 25.0

    return novelty

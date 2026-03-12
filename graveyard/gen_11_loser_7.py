"""
generator.py — Generation 0
Draws concentric circles with color progression and radiating lines.
This file is mutated by the evolution engine. All numeric literals are
intentional mutation targets.
"""
import math

def generate_svg():
    width = 500
    height = 500
    cx = 250.0
    cy = 250.0
    num_circles = 10
    max_radius = 200.0
    num_lines = 18
    line_length = 193.11
    stroke_width = 2.0
    bg_color = '#00233f'
    elements = []
    elements.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    elements.append(f'<rect width="{width}" height="{height}" fill="{bg_color}"/>')
    for i in range(0, num_lines, 3):
        angle = 2.0 * math.pi * i / num_lines
        for j in range(3, num_circles, 3):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#b8c0ff" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.11 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#a5fff6" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 4):
        angle = 1.56 * math.pi * i / num_lines
        for j in range(4, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#fffdff" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.23 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#b0ffff" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(30 + 225 * t)
        g = int(60 + 100 * (1.0 - t))
        b = int(180 + 75 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.15 + 0.05 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_lines):
        angle = 2.0 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 255)
        r = min(255, 80 + hue_shift)
        g = min(255, 40 + int(hue_shift * 0.5))
        b = max(0, 200 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.3 + 0.4 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="8.0" fill="#ffe9de" fill-opacity="0.9"/>')
    elements.append('</svg>')
    return '\n'.join(elements)
if __name__ == '__main__':
    print(generate_svg())
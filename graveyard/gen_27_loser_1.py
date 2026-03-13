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
    max_radius = 226.12
    num_lines = 16
    line_length = 193.11
    stroke_width = 2.35
    bg_color = '#00386a'
    elements = []
    elements.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    elements.append(f'<rect width="{width}" height="{height}" fill="{bg_color}"/>')
    for i in range(0, num_lines, 3):
        angle = 1.74 * math.pi * i / num_lines
        for j in range(5, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#c8ffff" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.03 * math.pi * i / num_lines
        for j in range(6, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#c8ffff" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(38 + 238 * t)
        g = int(43 + 81 * (0.72 - t))
        b = int(174 + 87 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.12 + 0.06 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 2):
        angle = 2.23 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#ece9cc" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 4):
        angle = 1.56 * math.pi * i / num_lines
        for j in range(4, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#a3ddff" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(36 + 152 * t)
        g = int(44 + 81 * (1.26 - t))
        b = int(174 + 59 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.19 + 0.06 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_lines):
        angle = 2.0 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 255)
        r = min(255, 80 + hue_shift)
        g = min(236, 40 + int(hue_shift * 0.5))
        b = max(0, 200 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.3 + 0.4 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 3):
        angle = 2.0 * math.pi * i / num_lines
        for j in range(3, num_circles, 3):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#a1ffbf" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.11 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#91c0f3" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 5):
        angle = 1.35 * math.pi * i / num_lines
        for j in range(5, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#aad6ff" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(43 + 197 * t)
        g = int(50 + 95 * (1.41 - t))
        b = int(212 + 47 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.17 + 0.04 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 4):
        angle = 1.37 * math.pi * i / num_lines
        for j in range(2, num_circles, 3):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#9fffd0" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(30 + 188 * t)
        g = int(60 + 100 * (1.0 - t))
        b = int(205 + 75 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.15 + 0.05 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 2):
        angle = 1.48 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#91c0f3" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 2.53 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 228)
        r = min(221, 57 + hue_shift)
        g = min(267, 45 + int(hue_shift * 0.57))
        b = max(0, 229 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.38 + 0.32 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(num_lines):
        angle = 2.15 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 167)
        r = min(254, 43 + hue_shift)
        g = min(304, 50 + int(hue_shift * 0.49))
        b = max(0, 274 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.26 + 0.37 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="8.0" fill="#dcdbf5" fill-opacity="0.9"/>')
    elements.append('</svg>')
    return '\n'.join(elements)
if __name__ == '__main__':
    print(generate_svg())
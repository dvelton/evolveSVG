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
    cy = 251.34
    num_circles = 12
    max_radius = 233.76
    num_lines = 15
    line_length = 193.11
    stroke_width = 2.57
    bg_color = '#00583c'
    elements = []
    elements.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    elements.append(f'<rect width="{width}" height="{height}" fill="{bg_color}"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(36 + 152 * t)
        g = int(44 + 81 * (1.26 - t))
        b = int(196 + 48 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.2 + 0.06 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(47 + 193 * t)
        g = int(38 + 61 * (1.07 - t))
        b = int(140 + 60 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.17 + 0.07 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 2):
        angle = 2.94 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#72a8be" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(42 + 189 * t)
        g = int(32 + 86 * (0.61 - t))
        b = int(249 + 61 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.13 + 0.07 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 3):
        angle = 1.09 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#c2e7b8" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 3):
        angle = 1.74 * math.pi * i / num_lines
        for j in range(5, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#96ffd6" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.1 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#d0d8fe" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 5):
        angle = 2.33 * math.pi * i / num_lines
        for j in range(8, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#b0d3ff" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(30 + 199 * t)
        g = int(67 + 100 * (0.81 - t))
        b = int(205 + 75 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.15 + 0.05 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 4):
        angle = 2.02 * math.pi * i / num_lines
        for j in range(6, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#b0dcfc" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 2.0 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 255)
        r = min(217, 80 + hue_shift)
        g = min(271, 40 + int(hue_shift * 0.46))
        b = max(0, 200 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.36 + 0.4 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(num_lines):
        angle = 2.33 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 301)
        r = min(319, 94 + hue_shift)
        g = min(195, 33 + int(hue_shift * 0.39))
        b = max(0, 227 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.23 + 0.35 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(num_lines):
        angle = 2.71 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 143)
        r = min(214, 50 + hue_shift)
        g = min(436, 35 + int(hue_shift * 0.56))
        b = max(0, 339 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.31 + 0.3 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 2):
        angle = 1.7 * math.pi * i / num_lines
        for j in range(4, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#79e7df" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.74 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#d3e4b8" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 2.53 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 272)
        r = min(221, 64 + hue_shift)
        g = min(267, 45 + int(hue_shift * 0.59))
        b = max(0, 229 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.38 + 0.32 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 2):
        angle = 2.67 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#b4c9fd" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 1.48 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#a0c3c8" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 1.33 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#8bbaec" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(29 + 192 * t)
        g = int(50 + 81 * (0.9 - t))
        b = int(215 + 75 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.23 + 0.04 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 4):
        angle = 1.37 * math.pi * i / num_lines
        for j in range(2, num_circles, 3):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#add9b9" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 5):
        angle = 1.35 * math.pi * i / num_lines
        for j in range(5, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#87c7f1" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.23 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#b6fdff" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.11 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#cfb6ff" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(43 + 197 * t)
        g = int(53 + 113 * (1.58 - t))
        b = int(212 + 47 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.17 + 0.04 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 4):
        angle = 1.56 * math.pi * i / num_lines
        for j in range(4, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#cbe9e8" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 3):
        angle = 2.0 * math.pi * i / num_lines
        for j in range(4, num_circles, 3):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#ddfcff" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(38 + 276 * t)
        g = int(31 + 76 * (0.72 - t))
        b = int(203 + 87 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.1 + 0.06 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(31 + 318 * t)
        g = int(30 + 59 * (0.61 - t))
        b = int(232 + 59 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.08 + 0.05 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_lines):
        angle = 2.15 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 180)
        r = min(254, 43 + hue_shift)
        g = min(315, 44 + int(hue_shift * 0.49))
        b = max(0, 274 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.26 + 0.37 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 4):
        angle = 2.26 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#adedd8" fill-opacity="0.6"/>')
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="8.0" fill="#d2fec4" fill-opacity="0.9"/>')
    elements.append('</svg>')
    return '\n'.join(elements)
if __name__ == '__main__':
    print(generate_svg())
"""
generator.py — Generation 0
Draws concentric circles with color progression and radiating lines.
This file is mutated by the evolution engine. All numeric literals are
intentional mutation targets.
"""
import math

def generate_svg():
    width = 422
    height = 426
    cx = 195.2
    cy = 205.1
    num_circles = 9
    max_radius = 249.66
    num_lines = 10
    line_length = 228.04
    stroke_width = 2.57
    bg_color = '#00a027'
    elements = []
    elements.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    elements.append(f'<rect width="{width}" height="{height}" fill="{bg_color}"/>')
    for i in range(0, num_lines, 2):
        angle = 3.44 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#6fbcde" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(34 + 175 * t)
        g = int(50 + 59 * (0.77 - t))
        b = int(146 + 75 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.23 + 0.04 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(29 + 218 * t)
        g = int(40 + 66 * (1.0 - t))
        b = int(127 + 66 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.28 + 0.05 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(42 + 142 * t)
        g = int(52 + 71 * (1.01 - t))
        b = int(240 + 55 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.24 + 0.07 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(48 + 114 * t)
        g = int(51 + 59 * (0.87 - t))
        b = int(300 + 41 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.27 + 0.08 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 4):
        angle = 1.95 * math.pi * i / num_lines
        for j in range(6, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#bdc5fa" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 3):
        angle = 2.26 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#5becc7" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 3):
        angle = 2.68 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#5becc7" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.7 * math.pi * i / num_lines
        for j in range(3, num_circles, 4):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#cdddba" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 3.27 * math.pi * i / num_lines
        for j in range(4, num_circles, 3):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#cdddba" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 3):
        angle = 2.68 * math.pi * i / num_lines
        for j in range(3, num_circles, 3):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#a1f9ab" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 4):
        angle = 3.47 * math.pi * i / num_lines
        for j in range(3, num_circles, 4):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#a1f9ab" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 4):
        angle = 3.41 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#a5d2b3" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(43 + 331 * t)
        g = int(21 + 66 * (0.82 - t))
        b = int(148 + 67 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.13 + 0.04 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 2):
        angle = 2.99 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#62baf7" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 5):
        angle = 1.1 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#dbfffa" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.1 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#f0fffe" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(36 + 76 * t)
        g = int(60 + 58 * (0.96 - t))
        b = int(149 + 40 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.2 + 0.02 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(26 + 63 * t)
        g = int(43 + 44 * (1.44 - t))
        b = int(150 + 32 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.22 + 0.02 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 4):
        angle = 0.89 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#c0edbd" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.09 * math.pi * i / num_lines
        for j in range(4, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#9cd4d2" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.69 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#cbffb2" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(29 + 93 * t)
        g = int(49 + 66 * (1.56 - t))
        b = int(188 + 46 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.25 + 0.02 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 4):
        angle = 1.67 * math.pi * i / num_lines
        for j in range(4, num_circles, 3):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#b1d3ff" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(39 + 102 * t)
        g = int(47 + 70 * (2.05 - t))
        b = int(189 + 34 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.19 + 0.03 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_lines):
        angle = 2.02 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 183)
        r = min(246, 42 + hue_shift)
        g = min(367, 46 + int(hue_shift * 0.49))
        b = max(0, 243 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.35 + 0.22 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(42 + 154 * t)
        g = int(32 + 86 * (0.61 - t))
        b = int(249 + 69 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.14 + 0.07 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(38 + 276 * t)
        g = int(25 + 76 * (0.72 - t))
        b = int(203 + 87 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.1 + 0.05 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(32 + 104 * t)
        g = int(44 + 68 * (1.26 - t))
        b = int(214 + 36 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.29 + 0.03 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 2):
        angle = 1.8 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#deffff" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(42 + 136 * t)
        g = int(36 + 90 * (1.43 - t))
        b = int(239 + 42 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.21 + 0.04 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 2):
        angle = 2.34 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#5bb3da" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(26 + 318 * t)
        g = int(30 + 52 * (0.61 - t))
        b = int(232 + 83 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.08 + 0.05 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(34 + 228 * t)
        g = int(31 + 67 * (1.13 - t))
        b = int(197 + 95 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.17 + 0.06 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(27 + 83 * t)
        g = int(57 + 84 * (1.67 - t))
        b = int(246 + 43 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.22 + 0.04 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 2):
        angle = 2.57 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#89abb9" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 2.71 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 143)
        r = min(214, 50 + hue_shift)
        g = min(436, 35 + int(hue_shift * 0.56))
        b = max(0, 339 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.36 + 0.27 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 5):
        angle = 1.28 * math.pi * i / num_lines
        for j in range(6, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#c4dccb" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 2.54 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 147)
        r = min(183, 111 + hue_shift)
        g = min(352, 52 + int(hue_shift * 0.54))
        b = max(0, 229 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.27 + 0.36 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 2):
        angle = 1.57 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#d7e6f7" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 5):
        angle = 2.47 * math.pi * i / num_lines
        for j in range(5, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#b2a0e4" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 1.64 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 291)
        r = min(243, 79 + hue_shift)
        g = min(340, 47 + int(hue_shift * 0.48))
        b = max(0, 161 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.23 + 0.49 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(num_lines):
        angle = 2.15 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 180)
        r = min(254, 37 + hue_shift)
        g = min(342, 48 + int(hue_shift * 0.42))
        b = max(0, 274 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.27 + 0.31 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 3):
        angle = 1.56 * math.pi * i / num_lines
        for j in range(4, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#c2eddc" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(30 + 199 * t)
        g = int(54 + 100 * (0.81 - t))
        b = int(205 + 75 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.15 + 0.05 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 2):
        angle = 1.7 * math.pi * i / num_lines
        for j in range(4, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#4aabdd" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(50 + 197 * t)
        g = int(53 + 96 * (1.66 - t))
        b = int(212 + 47 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.17 + 0.04 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(num_lines):
        angle = 2.53 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 272)
        r = min(184, 59 + hue_shift)
        g = min(267, 45 + int(hue_shift * 0.59))
        b = max(0, 229 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.42 + 0.32 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 2):
        angle = 4.02 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#88cfc9" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 4):
        angle = 1.74 * math.pi * i / num_lines
        for j in range(5, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#9edbc7" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.02 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#cffdf6" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 1.79 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#f1ffff" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 1.09 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#ffb89d" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 4):
        angle = 1.17 * math.pi * i / num_lines
        for j in range(2, num_circles, 3):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#bcd259" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.39 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#88cfc9" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 3.33 * math.pi * i / num_lines
        for j in range(4, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#62d6ed" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 3.32 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#8aa7c4" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.94 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#4da6e5" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.02 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#72c2dd" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(58 + 203 * t)
        g = int(22 + 45 * (1.29 - t))
        b = int(153 + 91 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.08 + 0.08 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 5):
        angle = 2.65 * math.pi * i / num_lines
        for j in range(8, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#86f5ff" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 2.33 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 277)
        r = min(319, 82 + hue_shift)
        g = min(195, 33 + int(hue_shift * 0.39))
        b = max(0, 227 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.23 + 0.4 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(num_lines):
        angle = 3.42 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 230)
        r = min(254, 29 + hue_shift)
        g = min(248, 72 + int(hue_shift * 0.61))
        b = max(0, 178 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.3 + 0.24 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 3):
        angle = 1.09 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#a2b860" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.67 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#5bb3da" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 3):
        angle = 2.21 * math.pi * i / num_lines
        for j in range(4, num_circles, 3):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#cdddba" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(34 + 73 * t)
        g = int(38 + 80 * (2.47 - t))
        b = int(220 + 24 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.15 + 0.04 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 3):
        angle = 2.21 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#95d191" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.77 * math.pi * i / num_lines
        for j in range(5, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#adedd8" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 1.82 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 140)
        r = min(348, 51 + hue_shift)
        g = min(383, 60 + int(hue_shift * 0.64))
        b = max(0, 238 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.35 + 0.38 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 2):
        angle = 2.3 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#b2ffbf" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 2.0 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 239)
        r = min(217, 102 + hue_shift)
        g = min(271, 40 + int(hue_shift * 0.43))
        b = max(0, 200 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.3 + 0.4 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(num_lines):
        angle = 2.25 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 299)
        r = min(240, 74 + hue_shift)
        g = min(315, 36 + int(hue_shift * 0.35))
        b = max(0, 227 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.35 + 0.29 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 2):
        angle = 2.23 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#a0f8fc" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 2.11 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#efaeff" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 2.02 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 106)
        r = min(278, 57 + hue_shift)
        g = min(561, 28 + int(hue_shift * 0.66))
        b = max(0, 260 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.23 + 0.34 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(36 + 152 * t)
        g = int(50 + 81 * (1.19 - t))
        b = int(196 + 48 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.2 + 0.06 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 4):
        angle = 1.35 * math.pi * i / num_lines
        for j in range(7, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#97d8e8" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 3.23 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 237)
        r = min(224, 77 + hue_shift)
        g = min(307, 35 + int(hue_shift * 0.7))
        b = max(0, 202 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.34 + 0.38 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 3):
        angle = 1.32 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#bfffdd" fill-opacity="0.6"/>')
    for i in range(0, num_lines, 2):
        angle = 1.48 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#b09b9d" fill-opacity="0.6"/>')
    for i in range(num_lines):
        angle = 2.35 * math.pi * i / num_lines
        x2 = cx + line_length * math.cos(angle)
        y2 = cy + line_length * math.sin(angle)
        hue_shift = int(i / num_lines * 161)
        r = min(318, 34 + hue_shift)
        g = min(276, 58 + int(hue_shift * 0.55))
        b = max(0, 242 - hue_shift)
        color = f'#{r:02x}{g:02x}{b:02x}'
        opacity = 0.27 + 0.29 * (i / num_lines)
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{stroke_width}" opacity="{opacity:.2f}"/>')
    for i in range(0, num_lines, 6):
        angle = 1.41 * math.pi * i / num_lines
        for j in range(3, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#c4e7f7" fill-opacity="0.6"/>')
    for i in range(num_circles, 0, -1):
        radius = max_radius * i / num_circles
        t = i / num_circles
        r = int(47 + 273 * t)
        g = int(27 + 56 * (1.44 - t))
        b = int(234 + 72 * math.sin(t * math.pi))
        color = f'#{r:02x}{g:02x}{b:02x}'
        fill_opacity = 0.12 + 0.06 * t
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{radius:.1f}" fill="{color}" fill-opacity="{fill_opacity:.2f}" stroke="{color}" stroke-width="1.5"/>')
    for i in range(0, num_lines, 2):
        angle = 2.75 * math.pi * i / num_lines
        for j in range(2, num_circles, 2):
            dot_r = max_radius * j / num_circles
            dx = cx + dot_r * math.cos(angle)
            dy = cy + dot_r * math.sin(angle)
            elements.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="3.0" fill="#2bb4be" fill-opacity="0.6"/>')
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="8.0" fill="#b2bfa6" fill-opacity="0.9"/>')
    elements.append('</svg>')
    return '\n'.join(elements)
if __name__ == '__main__':
    print(generate_svg())
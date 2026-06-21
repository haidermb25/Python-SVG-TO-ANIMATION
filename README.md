SVG Animation Generator (Python PIL)

This project converts SVG images into animated GIFs using Python by applying multiple custom animation effects such as movement, rotation, zoom, fade, and shake.

📖 About

A Python-based tool that converts SVG files into animated GIFs with multiple customizable animation styles.

🚀 Features
SVG to PNG conversion
Generate animated GIFs
Multiple animation styles:
Move (left/right, up/down)
Rotate (clockwise/counterclockwise)
Zoom & Scale
Fade in/out
Shake effects
Wobble & bounce
Custom frame control
Lightweight PIL-based processing
🛠️ Requirements
Python 3.x
Pillow (PIL)
CairoSVG
Math library (built-in)
📦 Installation
pip install pillow cairosvg
▶️ Usage
create_animated_gif(
    svg_path="input.svg",
    gif_path="output.gif",
    animation_style="zoom_in_out",
    frame_count=20
)
🎬 Supported Animation Styles
move_left_right
move_up_down
rotate_clockwise
rotate_counterclockwise
fade_in_out
zoom_in_out
scale_up_down
shake_left_right
shake_up_down
swing_rotation
hover_bounce
wobble

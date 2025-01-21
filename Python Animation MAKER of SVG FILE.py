from PIL import Image, ImageEnhance
import cairosvg
import math

# Convert SVG to PNG
def svg_to_png(svg_path, png_path):
    with open(svg_path, "rb") as svg_file:
        cairosvg.svg2png(file_obj=svg_file, write_to=png_path)

# Animation functions
def move_left_right(original, frame_count):
    frames = []
    width, height = original.size
    max_offset = width // 7

    for i in range(frame_count):
        offset = int(max_offset * math.sin(2 * math.pi * i / frame_count))
        frame = original.transform(original.size, Image.AFFINE, (1, 0, offset, 0, 1, 0))
        frames.append(frame)

    return frames


def move_up_down(original, frame_count):
    frames = []
    width, height = original.size
    max_offset = width // 10
    for i in range(frame_count):
        offset = int(max_offset * math.sin(2 * math.pi * i / frame_count))
        frame = original.transform(original.size, Image.AFFINE, (1, 0, 0, 0, 1, offset))
        frames.append(frame)
    return frames

def rotate_clockwise(original, frame_count):
    frames = []
    for i in range(frame_count):
        frame = original.rotate(-i * (360 / frame_count))
        frames.append(frame)
    return frames

def rotate_counterclockwise(original, frame_count):
    frames = []
    for i in range(frame_count):
        frame = original.rotate(-i * (360 / frame_count))
        frames.append(frame)
    return frames

def fade_in_out(original, frame_count):
    frames = []
    enhancer = ImageEnhance.Brightness(original)
    for i in range(frame_count):
        brightness = abs(math.sin(2 * math.pi * i / frame_count))
        frame = enhancer.enhance(brightness)
        frames.append(frame)
    return frames


def zoom_in_out(original, frame_count):
    frames = []
    max_scale = 0.3

    for i in range(frame_count):
        scale_factor = 1 + max_scale * math.sin(2 * math.pi * i / frame_count)
        new_width = int(original.width * scale_factor)
        new_height = int(original.height * scale_factor)
        frame = original.resize((new_width, new_height), Image.LANCZOS)
        new_frame = Image.new("RGBA", original.size, (255, 255, 255, 0))
        x_offset = (new_frame.width - frame.width) // 2
        y_offset = (new_frame.height - frame.height) // 2
        new_frame.paste(frame, (x_offset, y_offset), frame)
        frames.append(new_frame)

    return frames

def scale_up_down(original, frame_count):
    frames = []
    for i in range(frame_count):
        scale_factor = 0.8 + 0.4 * abs(math.sin(2 * math.pi * i / frame_count))
        frame = original.resize((int(original.width * scale_factor), int(original.height * scale_factor)), Image.LANCZOS)
        frames.append(frame)
    return frames

def shake_left_right(original, frame_count):
    frames = []
    for i in range(frame_count):
        offset = int(3 * math.sin(2 * math.pi * i * 5 / frame_count))  # Faster shake
        frame = original.transform(original.size, Image.AFFINE, (1, 0, offset, 0, 1, 0))
        frames.append(frame)
    return frames

def shake_up_down(original, frame_count):
    frames = []
    for i in range(frame_count):
        offset = int(3 * math.sin(2 * math.pi * i * 5 / frame_count))  # Faster shake
        frame = original.transform(original.size, Image.AFFINE, (1, 0, 0, 0, 1, offset))
        frames.append(frame)
    return frames

def swing_rotation(original, frame_count):
    frames = []
    for i in range(frame_count):
        angle = 10 * math.sin(2 * math.pi * i / frame_count)
        frame = original.rotate(angle)
        frames.append(frame)
    return frames

def hover_bounce(original, frame_count):
    frames = []
    max_offset = 10

    for i in range(frame_count):
        offset = int(max_offset * abs(math.sin(2 * math.pi * i / frame_count)))
        frame = original.transform(original.size, Image.AFFINE, (1, 0, 0, 0, 1, -offset))
        frames.append(frame)

    return frames



def wobble(original, frame_count):
    frames = []
    for i in range(frame_count):
        angle = 5 * math.sin(2 * math.pi * i / frame_count)
        scale_factor = 1 + 0.1 * math.sin(2 * math.pi * i * 2 / frame_count)
        frame = original.rotate(angle).resize(
            (int(original.width * scale_factor), int(original.height * scale_factor)),
            Image.LANCZOS
        )
        frames.append(frame)
    return frames

def create_animated_gif(svg_path, gif_path, animation_style, frame_count=20):
    png_path = "temp.png"
    svg_to_png(svg_path, png_path)
    original = Image.open(png_path)

    # Select animation based on user input
    if animation_style == "move_left_right":
        frames = move_left_right(original, frame_count)
    elif animation_style == "move_up_down":
        frames = move_up_down(original, frame_count)
    elif animation_style == "rotate_clockwise":
        frames = rotate_clockwise(original, frame_count)
    elif animation_style == "rotate_counterclockwise":
        frames = rotate_counterclockwise(original, frame_count)
    elif animation_style == "fade_in_out":
        frames = fade_in_out(original, frame_count)
    elif animation_style == "zoom_in_out":
        frames = zoom_in_out(original, frame_count)
    elif animation_style == "scale_up_down":
        frames = scale_up_down(original, frame_count)
    elif animation_style == "shake_left_right":
        frames = shake_left_right(original, frame_count)
    elif animation_style == "shake_up_down":
        frames = shake_up_down(original, frame_count)
    elif animation_style == "swing_rotation":
        frames = swing_rotation(original, frame_count)
    elif animation_style == "hover_bounce":
        frames = hover_bounce(original, frame_count)
    elif animation_style == "wobble":
        frames = wobble(original, frame_count)
    else:
        print("Animation style not recognized.")
        return

    # Save frames as GIF
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=100, loop=0)

# Example usage
svg_path = "/content/GIFAnimationFolder/Ramadan.svg"
gif_path = "/content/zoom_in_out.gif"
animation_style = "zoom_in_out"  # Change this to try different animations
create_animated_gif(svg_path, gif_path, animation_style)

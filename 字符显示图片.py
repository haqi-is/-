
import os
from PIL import Image
from rich.console import Console
def show_char(image_path,width=100):
    ascii_chars = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft|()1{}[]?-_+~<>i!lI;:,"^`'. '''  # "█■▣#▪+=▫-. "  # 至少包含 11 个字符"█▩▦▣▪▫    "
    image = Image.open(image_path).convert("L")  # 确保是灰度图
    aspect_ratio = image.height / image.width
    new_height = int(aspect_ratio * width * 0.55)
    image = image.resize((width, new_height))
    pixels = image.getdata()
    scale_factor = len(ascii_chars) - 1
    # ascii_str = "".join([ascii_chars[pixel // (256 // scale_factor)] for pixel in pixels])
    ascii_str = "".join([ascii_chars[min(int(pixel / (255 / scale_factor)), scale_factor)] for pixel in pixels])
    ascii_lines = [ascii_str[i:i + width] for i in range(0, len(ascii_str), width)]

    console = Console()
    ascii_art = ascii_lines
    for line in ascii_art:
        console.print(line)
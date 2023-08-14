from PIL import Image
import os

# Define colors
colors = [
    (255, 0, 0),      # Red
    (0, 0, 255),      # Blue
    (0, 255, 0),      # Green
    (255, 255, 0),    # Yellow
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
    (255, 192, 203),  # Pink
    (0, 255, 255),    # Cyan
    (255, 255, 255),  # White
    (0, 0, 0)         # Black
]

# Define resolutions
resolutions = [
    (512, 512),
    (1024, 1024),
    (2048, 2048),
    (720, 480),
    (480, 720),
    (1920, 1080),
    (1080, 1920),
    (3840, 2160),
    (2160, 3840)
]

# Directory to save images
output_dir = "/mnt/data/color_images/"

# Create directory if not exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create images for each color and resolution
file_paths = []
for color in colors:
    for resolution in resolutions:
        image = Image.new("RGB", resolution, color)
        file_name = f"{color[0]}_{color[1]}_{color[2]}_{resolution[0]}x{resolution[1]}.png"
        file_path = os.path.join(output_dir, file_name)
        image.save(file_path)
        file_paths.append(file_path)


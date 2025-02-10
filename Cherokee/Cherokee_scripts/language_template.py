import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# File paths
input_file = r" "  # Path to your CSV file
output_dir = r" "  # Path to your directory
font_path_english = r"C:\Windows\Fonts\Gadugi.ttf"
font_path_cherokee = r"C:\Users\user\Downloads\anowelisgv1-2.ttf"
font_size = 32

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Load the CSV
df = pd.read_csv(input_file, encoding='latin1')  # or 'windows-1252'

# Process each row
for index, row in df.iterrows():
    english_word = row['English']
    cherokee_symbols = row['Cherokee Symbols']
    cherokee_word = row['Cherokee Word']

    # Create an image for the row
    img = Image.new('RGB', (800, 150), color=(255, 255, 255))  # White background
    draw = ImageDraw.Draw(img)

    # Draw English word
    font_english = ImageFont.truetype(font_path_english, font_size)
    draw.text((10, 10), f"English: {english_word}", font=font_english, fill=(0, 0, 0))

    # Draw Cherokee symbols
    font_cherokee = ImageFont.truetype(font_path_cherokee, font_size)
    draw.text((10, 50), f"Cherokee Symbols: {cherokee_symbols}", font=font_cherokee, fill=(0, 0, 0))

    # Draw Cherokee word
    draw.text((10, 90), f"Cherokee Word: {cherokee_word}", font=font_cherokee, fill=(0, 0, 0))

    # Save the image
    img.save(os.path.join(output_dir, f"row_{index + 1}.png"))

print(f"Generated {len(df)} images in {output_dir}")

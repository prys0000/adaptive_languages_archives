import pandas as pd
import os

# Paths
input_file = r" "  # Path to your CSV file
image_dir = r" "  # Directory with generated images
output_gt_dir = r"G:\Cherokee\cherokee_ground_truth"  # Directory for .gt.txt files

# Create output directory if it doesn't exist
os.makedirs(output_gt_dir, exist_ok=True)

# Load the CSV
df = pd.read_csv(input_file, encoding='latin1')  # or 'windows-1252'

# Generate .gt.txt files for each image
for index, row in df.iterrows():
    gt_file_path = os.path.join(output_gt_dir, f"row_{index + 1}.gt.txt")
    with open(gt_file_path, 'w', encoding='utf-8') as gt_file:
        # Combine English, Cherokee Symbols, and Cherokee Word
        ground_truth = f"{row['English']} {row['Cherokee Symbols']} {row['Cherokee Word']}"
        gt_file.write(ground_truth)

print(f"Generated {len(df)} ground truth files in {output_gt_dir}")

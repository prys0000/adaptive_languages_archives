import os
import subprocess

# Paths to your image and output directories
image_dir = r"G:\Cherokee\cherokee_ground_truth"
output_dir = r"G:\Cherokee\ltmsf"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate through all .png files
for image_file in os.listdir(image_dir):
    if image_file.endswith(".png"):
        base_name = os.path.splitext(image_file)[0]
        txt_file = os.path.join(image_dir, f"{base_name}.txt")
        output_file = os.path.join(output_dir, base_name)
        
        # Check if corresponding .txt exists
        if os.path.exists(txt_file):
            print(f"Processing {image_file} with transcription {txt_file}")
            try:
                subprocess.run([
                    "tesseract",
                    os.path.join(image_dir, image_file),
                    output_file,
                    "--psm", "6",
                    "lstm.train"
                ], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error processing {image_file}: {e}")
        else:
            print(f"Missing transcription file for {image_file}")

import pytesseract
from PIL import Image
import os

# Path to Tesseract OCR executable (update with your path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the traineddata file
traineddata_dir = r'C:\Program Files\Tesseract-OCR\tessdata'
model_name = 'cherokee'

# Check if the traineddata file is in the tessdata directory
traineddata_file = os.path.join(traineddata_dir, f'{model_name}.traineddata')
if not os.path.exists(traineddata_file):
    raise FileNotFoundError(f"The traineddata file {traineddata_file} does not exist. Please place it in the tessdata directory.")

# Input image directory and output text directory
input_image_dir = r' '  # Update to your image directory
output_text_dir = r' '  # Update to your desired output directory
os.makedirs(output_text_dir, exist_ok=True)

# OCR configuration
custom_oem_psm_config = f'--oem 1 --psm 6 -l {model_name}'

# Process images in the input directory
for filename in os.listdir(input_image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        image_path = os.path.join(input_image_dir, filename)
        output_text_path = os.path.join(output_text_dir, f'{os.path.splitext(filename)[0]}.txt')

        # Perform OCR
        try:
            with Image.open(image_path) as img:
                print(f"Processing {filename}...")
                text = pytesseract.image_to_string(img, config=custom_oem_psm_config)

            # Save OCR result to a text file
            with open(output_text_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

            print(f"OCR completed for {filename}. Output saved to {output_text_path}")

        except Exception as e:
            print(f"Failed to process {filename}: {e}")

print("All images processed.")

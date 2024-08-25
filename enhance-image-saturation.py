import os
import sys
from PIL import Image, ImageEnhance

def enhance_image(file_path, enhancement_factor, brightness_factor, contrast_factor, max_dimension):
    try:
        img = Image.open(file_path)

        # Enhance color/saturation
        color_converter = ImageEnhance.Color(img)
        img = color_converter.enhance(enhancement_factor)

        # Enhance brightness
        brightness_converter = ImageEnhance.Brightness(img)
        img = brightness_converter.enhance(brightness_factor)

        # Enhance contrast
        contrast_converter = ImageEnhance.Contrast(img)
        img = contrast_converter.enhance(contrast_factor)

        # Resize image proportionally
        width, height = img.size
        if width > height:
            new_width = max_dimension
            new_height = int((max_dimension / width) * height)
        else:
            new_height = max_dimension
            new_width = int((max_dimension / height) * width)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Append "_enhanced" before the file extension
        base, ext = os.path.splitext(file_path)
        new_file_path = f"{base}_enhanced{ext}"

        img.save(new_file_path)
        print(f"Enhanced image saved as: {new_file_path}")
    except Exception as e:
        print(f"")
        print(f"************************************************")
        print(f"********* {file_path}: {e}")
        print(f"Error processing file {file_path}: {e}")
        print(f"*************************************************")
        print(f"")



def process_directory(directory_path, enhancement_factor, brightness_factor, contrast_factor, max_dimension):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
            file_path = os.path.join(directory_path, filename)
            enhance_image(file_path, enhancement_factor, brightness_factor, contrast_factor, max_dimension)

def main():
    if len(sys.argv) < 6:
        print("Usage: python enhance_image.py <file_or_directory_path> <enhancement_factor> <brightness_factor> <contrast_factor> <max_dimension>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        enhancement_factor = float(sys.argv[2])
        brightness_factor = float(sys.argv[3])
        contrast_factor = float(sys.argv[4])
        max_dimension = int(sys.argv[5])
        print(f"Enhancement factor: {enhancement_factor}, Brightness factor: {brightness_factor}, Contrast factor: {contrast_factor}, Max dimension: {max_dimension}px")
    except ValueError:
        print("The enhancement, brightness, contrast factors must be numbers, and max dimension must be an integer.")
        sys.exit(1)

    if os.path.isdir(path):
        print(f"Processing directory: {path}")
        process_directory(path, enhancement_factor, brightness_factor, contrast_factor, max_dimension)
    elif os.path.isfile(path):
        print(f"Processing file: {path}")
        enhance_image(path, enhancement_factor, brightness_factor, contrast_factor, max_dimension)
    else:
        print("The specified path is neither a file nor a directory.")
        sys.exit(1)

if __name__ == "__main__":
    main()

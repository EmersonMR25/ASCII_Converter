import cv2 as cv
import sys
import os
import numpy as np

def convert_images_to_ascii(input_dir="src/Input", output_dir="src/Output", size_scale=0.3):
    # Check if the input directory exists
    if not os.path.exists(input_dir):
        sys.exit(f"Input directory '{input_dir}' does not exist.")
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # ASCII characters for different gray levels
    char_array = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>',
                  '<', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|',
                  '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y',
                  'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b',
                  'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']
    num_chars = len(char_array)

    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        
        # Check if file is an image
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):
            continue
        
        # Load the image
        img = cv.imread(input_path)
        if img is None:
            print(f"Could not read image: {filename}")
            continue

        # Convert to grayscale
        gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Resize the image
        new_width = int(gray_image.shape[1] * size_scale)
        new_height = int(gray_image.shape[0] * size_scale)
        gray_image = cv.resize(gray_image, (new_width, new_height))

        # Convert to ASCII
        ascii_image = np.full(gray_image.shape, ' ', dtype=str)
        for i in range(gray_image.shape[0]):
            for j in range(gray_image.shape[1]):
                # Perform multiplication in int32 to prevent overflow
                intensity = int(gray_image[i, j]) * (num_chars - 1) // 255
                ascii_image[i, j] = char_array[intensity]


        # Convert ASCII array to string
        ascii_text = "\n".join("".join(row) for row in ascii_image)

        # Save ASCII text to output file
        output_filename = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(output_dir, output_filename)
        with open(output_path, "w") as f:
            f.write(ascii_text)
        
        print(f"ASCII image saved at: {output_path}")

# Usage
convert_images_to_ascii()

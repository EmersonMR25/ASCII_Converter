import cv2 as cv
import sys
import os
import numpy as np

# Load the image
# The image is read from the specified file path. `cv.samples.findFile` is used to ensure
# that the path is correctly resolved across different environments.
img = cv.imread(cv.samples.findFile("src/Im_Input/Ronaldo_2024.webp"))

# Check if the image was successfully loaded
# If `img` is None, it means the image could not be loaded. This check prevents the
# program from proceeding with invalid data and exits with an error message.
if img is None:
    sys.exit("Could not read the image.")

# Resize the image for smaller processing
# A scaling factor is defined to resize the image, which helps in reducing the image's
# size for faster processing and easier handling.
size_scale = 0.2

# Convert the image to grayscale
# The `cv.cvtColor` function converts the image from color (BGR) to grayscale. This simplifies
# the processing by reducing the image to a single channel representing intensity.
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Calculate new dimensions and convert to integers
# The new width and height of the image are calculated based on the scaling factor.
# The dimensions are multiplied by the scaling factor and converted to integers
# because OpenCV requires integer dimensions for resizing.
new_width = int(gray_image.shape[1] * size_scale)
new_height = int(gray_image.shape[0] * size_scale)

# Resize the grayscale image
# The `cv.resize` function resizes the grayscale image to the new dimensions specified.
# It uses bilinear interpolation by default, which is suitable for resizing images.
gray_image = cv.resize(gray_image, (new_width, new_height))

# ASCII characters to use (more characters for better detail)
# A list of ASCII characters that will be used to represent different levels of gray intensity.
# Characters with more visual weight are used for darker areas, and lighter characters for brighter areas.
char_array = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>',
              '<', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|',
              '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y',
              'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b',
              'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']

# Create an ASCII image array
# An empty ASCII image array is created with the same dimensions as the resized grayscale image.
# Each pixel in the ASCII image will be represented by an ASCII character.
ascii_image = np.full(gray_image.shape, ' ', dtype=str)

# Normalize the grayscale values to match the ASCII character set
# `num_chars` is the number of different ASCII characters available. The grayscale values
# (0-255) are normalized to the index range of the `char_array` to match the grayscale intensity.
num_chars = len(char_array)

for i in range(gray_image.shape[0]):
    for j in range(gray_image.shape[1]):
        # Normalize grayscale value to the range of ASCII characters
        # Each pixel’s grayscale value is mapped to an ASCII character based on its intensity.
        ascii_image[i, j] = char_array[gray_image[i, j] * (num_chars - 1) // 255]

# Convert ASCII array to a string and save as text file
# The ASCII image array is converted to a string where each row is joined by an empty string
# and each row is separated by a newline character. This string representation will be saved to a file.
ascii_text = "\n".join("".join(row) for row in ascii_image)

# Display the grayscale image
# The resized grayscale image is displayed in a window using OpenCV's `imshow` function.
# The window will stay open until a key is pressed.
cv.imshow("Gray Image", gray_image)
k = cv.waitKey(0)

# Save the ASCII image in the 'Output' folder if 's' key is pressed
# If the 's' key is pressed, the ASCII representation of the image will be saved to a text file.
if k == ord("s"):
    # Define the output directory
    # The directory where the ASCII text file will be saved is specified. If it does not exist,
    # it will be created.
    output_dir = "src/IM_Output"
    
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the full path for the ASCII text file
    # The path where the ASCII text file will be saved is constructed.
    output_path = os.path.join(output_dir, "RONALDO.txt")
    
    # Save the ASCII text
    # The ASCII text is written to the file. The file will be created if it does not exist,
    # or overwritten if it does.
    with open(output_path, "w") as f:
        f.write(ascii_text)

    # Print confirmation message
    # A message is printed to indicate the successful saving of the ASCII text file.
    print(f"ASCII image saved at: {output_path}")

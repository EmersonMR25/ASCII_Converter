import cv2 as cv
import sys
import os

# Load the image
img = cv.imread(cv.samples.findFile("src/Im_Input/Ronaldo_2024.webp"))

# Check if the image was successfully loaded
if img is None:
    sys.exit("Could not read the image.")



# Display the image in a window
cv.imshow("Display window", img)

k = cv.waitKey(0)

# Save the image in the 'Output' folder if 's' key is pressed
if k == ord("s"):
    # Define the output directory
    output_dir = "src/IM_Output"
    
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the full path for the output image
    output_path = os.path.join(output_dir, "RONALDO.png")
    
    # Save the image
    cv.imwrite(output_path, img)

    print(f"Image saved at: {output_path}")

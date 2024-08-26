# Image to ACII converter

# Image Processing with OpenCV library

## Description

This project consists of two Python scripts:

1. **`movement_capture.py`**: Captures and processes video to detect and display moving objects using OpenCV. It tracks motion in a video stream and highlights moving objects with bounding boxes.

2. **`ascii_editor.py`**: Converts an image into an ASCII representation and saves it as a text file. The script loads an image, converts it to grayscale, resizes it, and maps grayscale values to ASCII characters for textual representation.

## Requirements

- Python 3.x
- OpenCV (`opencv-python` and `opencv-python-headless`)
- NumPy (`numpy`)

You can install the required libraries using pip:

```bash
pip install opencv-python opencv-python-headless numpy
```

## Libraries Used

- OpenCV: For image processing and computer vision tasks.
- NumPy: For handling arrays and numerical operations.

## movement_capture.py

### Description

This script processes a video file or webcam feed to detect and highlight moving objects. It uses background subtraction to identify changes in the scene and draws bounding boxes around detected moving objects.

### How to Run

Ensure you have all required libraries installed.

Run the script using Python:

```bash
python movement_capture.py
```

Press 'q' to exit the video stream.
Press 's' to save the output image with detected movements.

## ascii_editor.py

### Description

This script converts an image into an ASCII art representation. It reads an image file, converts it to grayscale, resizes it for easier processing, and maps the grayscale values to a set of ASCII characters. The result is saved as a text file.

How to Run
Ensure you have all required libraries installed.

Modify the script to point to your image file.

Run the script using Python:

```bash
python ascii_editor.py
```

Press 's' to save the ASCII representation as a text file in the specified output directory.

## Notes

Ensure the paths to image files or video streams are correctly specified in the scripts.
Adjust the scaling factor in ascii_editor.py and video processing parameters in movement_capture.py according to your needs.
License
This project is licensed under the MIT License. See the LICENSE file for details.

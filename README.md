# Image Processing with OpenCV library

## Description

**`ascii_editor.py`**: Converts an image into an ASCII representation and saves it as a text file. The script loads an image, converts it to grayscale, resizes it, and maps grayscale values to ASCII characters for textual representation.

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

## app.py

### Description

This script converts an image into an ASCII art representation. It reads an image file, converts it to grayscale, resizes it for easier processing, and maps the grayscale values to a set of ASCII characters. The result is saved as a text file.

How to Run
Ensure you have all required libraries installed.

Add your desired images to the Input directory

Run the script using Python:

```bash
python app.py
```

## Notes

Ensure the paths to image files or video streams are correctly specified in the scripts.
Adjust the scaling factor in app.py and video processing parameters in movement_capture.py according to your needs.
License
This project is licensed under the MIT License. See the LICENSE file for details.

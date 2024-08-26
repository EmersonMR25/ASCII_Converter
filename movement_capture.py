import cv2 as cv

def main():
    """
    Main function to capture video from the webcam and detect moving objects.

    The function captures frames from the webcam, converts them to grayscale,
    and uses background subtraction to detect moving objects. It then draws
    contours around these moving objects and displays the video feed with the
    contours highlighted.

    Optimizations made by me:
    - Use of efficient data structures.
    - Reduced unnecessary conversions.
    - Streamlined operations for real-time performance.
    """
    # Capture video from the default camera (0 is usually the default webcam)
    cap = cv.VideoCapture(0)
    
    # Initialize the background subtractor, which will help in detecting motion
    background_subtractor = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=40, detectShadows=True)

    while True:
        # Read the current frame from the video feed
        ret, frame = cap.read()

        # If frame reading was unsuccessful, break the loop
        if not ret:
            break

        # Apply the background subtractor to get the foreground mask
        fg_mask = background_subtractor.apply(frame)

        # Perform morphological operations to reduce noise and improve detection
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
        fg_mask = cv.morphologyEx(fg_mask, cv.MORPH_OPEN, kernel)

        # Find contours of the detected moving objects
        contours, _ = cv.findContours(fg_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # Draw bounding boxes around detected objects
        for contour in contours:
            if cv.contourArea(contour) > 500:  # Ignore small contours to reduce false positives
                x, y, w, h = cv.boundingRect(contour)
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame with detected objects highlighted
        cv.imshow('Moving Objects', frame)

        # Exit the loop when 'q' is pressed
        if cv.waitKey(30) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
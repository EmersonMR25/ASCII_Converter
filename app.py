import cv2, time

first_frame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_delta = cv2.threshold(delta_frame, 30, 225, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countours in cnts:
        if cv2.contourArea(countours) < 10000:
            continue
        status = 1
        (x, y, h, w) = cv2.boundingRect(countours)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Capturing", gray)
    cv2.imshow("Gray Frame", delta_frame)
    cv2.imshow("Image Threshhold", thresh_delta)
    cv2.imshow("Color Frame", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    print(status)
video.release()
cv2.destroyAllWindows
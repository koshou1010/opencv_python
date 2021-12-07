import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(1) == ord('a'):
        break


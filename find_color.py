import cv2 
import numpy as np
from PIL import Image

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")
cv2.createTrackbar("Lower H", "Trackbars", 0, 360, nothing)
cv2.createTrackbar("Lower S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Lower V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Upper H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("Upper S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Upper V", "Trackbars", 255, 255, nothing)


while True:
    ret, frame = cap.read()
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    l_h = cv2.getTrackbarPos("Lower H", "Trackbars")
    l_s = cv2.getTrackbarPos("Lower S", "Trackbars")
    l_v = cv2.getTrackbarPos("Lower V", "Trackbars")
    u_h = cv2.getTrackbarPos("Upper H", "Trackbars")
    u_s = cv2.getTrackbarPos("Upper S", "Trackbars")
    u_v = cv2.getTrackbarPos("Upper V", "Trackbars")

    # mIn = np.array([10, 200, 100])
    # mAx = np.array([40, 250, 200])
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv_img, lower, upper)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    print(bbox)
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv2.imshow('MASK OUTPUT', mask)
    cv2.imshow('FRAME OUTPUT', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
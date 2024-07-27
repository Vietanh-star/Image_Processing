import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # for red color
    lowerRed = np.array([167, 139, 102])
    upperRed = np.array([179, 255, 255])

    #for yellow color
    lowerYellow = np.array([20, 71, 135])
    upperYellow = np.array([51, 255, 255])

    #for blue color
    lowerBlue = np.array([96, 92, 111])
    upperBlue = np.array([152, 255, 255])

    maskRed = cv2.inRange(img_hsv, lowerRed, upperRed)
    maskYellow = cv2.inRange(img_hsv, lowerYellow, upperYellow)
    maskBlue = cv2.inRange(img_hsv, lowerBlue, upperBlue)
    cv2.imshow("MaskRed", maskRed)
    cv2.imshow("Mask Yellow", maskYellow)
    cv2.imshow("Mask Blue", maskBlue)

    # _, mask1 = cv2.threshold(mask, 155, 255, cv2.THRESH_BINARY)
    # cv2.imshow("Threshold", mask1)

    countRed, _ = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    countBlue, _ = cv2.findContours(maskBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    numberRedObject = 0
    for redObject in countRed:
        x = 1000
        if cv2.contourArea(redObject) > x:
            x, y, w, h = cv2.boundingRect(redObject)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            numberRedObject += 1
            cv2.putText(frame, ("RED-{} ({}, {})".format(numberRedObject,x,y)), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    numberBlueObject = 0
    for blueObject in countBlue:
        x = 1000
        if cv2.contourArea(blueObject) > x:
            x, y, w, h = cv2.boundingRect(blueObject)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            numberBlueObject += 1
            cv2.putText(frame, ("BLUE-{} ({}, {})".format(numberBlueObject,x,y)), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
#     cont_img = cv2.drawContours(frame, countRed, -1, 255, 3)
#     cv2.imshow("RESULT", cont_img)

    cv2.imshow("RESULT", frame)
    print("number red object :", numberRedObject, "  ,  number blue object :", numberBlueObject)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
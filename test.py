import cv2
import datetime
import imutils
cam = cv2.VideoCapture('2.mkv')
print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

ret, Frame1 = cam.read()
ret, Frame2 = cam.read()
while(cam.isOpened()):

    diff = cv2.absdiff(Frame1,Frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 30,150)
    cnts = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:

        (x,y,w,h) = cv2.boundingRect(c)

        if cv2.contourArea(c) < 700:
            continue
        cv2.rectangle(Frame1, (x,y), (x+w, y+h), (0,255,0),2)




    cv2.imshow('Frame1', Frame1)
    Frame1 = Frame2
    ret, Frame2 = cam.read()


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()



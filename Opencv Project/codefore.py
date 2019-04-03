import cv2
import numpy as np
cap = cv2.VideoCapture(0)
# def make_480p():
#     cap.set(3,640)
#     cap.set(4,480)
# def make_720p():
#     cap.set(3,1280)
#     cap.set(4,720)
# def make_1080p():
#     cap.set(3,1920)
#     cap.set(4,1080)
# make_720p()
# def rescale_frame(frame,percent=75):
#     scale_percent=percent
#     width = int(frame.shape[1]*scale_percent/100)
#     height = int(frame.shape[0]*scale_percent/100)
#     dim = (width,height)
#     return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
while True:
    ret, frame = cap.read()
    frame1 = rescale_frame(frame,percent=30)
    cv2.imshow("llb",frame1)
    frame2 = rescale_frame(frame,percent=100)
    cv2.imshow("second",frame2)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
#when everything is done release the capture
cap.release()
cv2.destroyAllWindows()
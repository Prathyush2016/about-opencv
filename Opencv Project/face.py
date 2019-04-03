import cv2
import numpy
#BASICS OF ONENCV
#####################################
# img = cv2.imread("C:\\Users\\skyrangers\\PycharmProjects\\projectno1\\1.png",1)
#####################################
# print(type(img))
# print(img.shape)
# print(img)
#####################################
# cv2.imshow("deku",img)
# cv2.waitKey(0)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()
#####################################
# Resizeing the img
# resized = cv2.resize(img,(600,600))
# cv2.imshow("deku",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# After resizing the shape of the picture , the picture wont be symitric so we need to divide the pixel
# ######################################
# Dividing the img based on the pixel size
# resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# cv2.imshow("deku",resized)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()
#########################################
#FACEDETECTION
#########################################\

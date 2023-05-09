import cv2
import numpy as np

img=cv2.imread("colorful.png")
#q1

cv2.imshow("rose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#q2
blue_channel, green_channel, red_channel = cv2.split(img)
#q3


cv2.imshow("Blue Channel", blue_channel)
cv2.imshow("Green Channel", green_channel)
cv2.imshow("Red Channel", red_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()
#q4

green_channel[:] = 0
#q5

modified_image = cv2.merge((blue_channel, green_channel, red_channel))
#q6

cv2.imshow("Modified Image", modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#q7

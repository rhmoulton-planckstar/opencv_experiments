import cv2, numpy as np

img = cv2.imread("/Users/Rich/RandomShirt.png", 0)
cv2.imwrite("canny.png", cv2.Canny(img, 200, 300))
cv2.imshow("canny", cv2.imread("canny.png"))
cv2.waitKey()
cv2.destroyAllWindows()

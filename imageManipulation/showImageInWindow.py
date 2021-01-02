import cv2, numpy as np

img = cv2.imread('/Users/Rich/RandomShirt.png')
cv2.imshow('Random Shirt', img)
cv2.waitKey()
cv2.destroyAllWindows() 

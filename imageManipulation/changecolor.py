import cv2

img = cv2.imread('/Users/Rich/Pictures/me_red.jpeg')
img[:,:,0] = 0
cv2.imwrite('/Users/Rich/RandomShirt2.png', img)

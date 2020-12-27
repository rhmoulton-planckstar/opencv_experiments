import cv2

img = cv2.imread('/Users/Rich/RandomBlack.png')
img.itemset((150, 120, 0), 255)
cv2.imwrite('/Users/Rich/RandomBlueChannel.png', img)

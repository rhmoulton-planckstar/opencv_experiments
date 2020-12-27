import cv2, numpy

blackImage = numpy.zeros((3,3), dtype=numpy.uint8)
cv2.imwrite('/Users/Rich/3by3black.png', blackImage)

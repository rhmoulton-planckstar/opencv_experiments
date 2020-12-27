import cv2, numpy, os

randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray  = numpy.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('/Users/Rich/RandomGray.png', grayImage)

bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('/Users/Rich/RandomColor.png', bgrImage)

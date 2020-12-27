import cv2

cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
success, frame = cameraCapture.read()
success, frame = cameraCapture.read()
success, frame = cameraCapture.read()
success, frame = cameraCapture.read()
h, w = frame.shape[:2]
size = (w, h)
videoWriter = cv2.VideoWriter('/Users/Rich/Desktop/test2.mp4', cv2.VideoWriter_fourcc('X','2','6','4'),fps,size)
numFramesRemaining = 10 * fps - 1
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1
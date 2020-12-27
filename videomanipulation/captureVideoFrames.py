import cv2

def warmupCamera(camera):
  success, frame = camera.read()
  success, frame = camera.read()
  success, frame = camera.read()
  success, frame = camera.read()
  return camera.read()

def getTrueSize(theFrame):
  h, w = theFrame.shape[:2]
  return (w, h)

runTime = 10 // Seconds
fps = 30
numFramesRemaining = runTime * fps - 1

// Init reader
cameraCapture = cv2.VideoCapture(0)

// The following line is unreliable
//size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

success, frame = warmupCamera(cameraCapture)
size = getTrueSize(frame)

// Init writer
videoWriter = cv2.VideoWriter('/Users/Rich/Desktop/test2.mp4', cv2.VideoWriter_fourcc('X','2','6','4'),fps,size)

// Record all the things!!!
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1

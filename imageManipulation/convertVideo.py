import cv2

// Prepare input
videoCapture = cv2.VideoCapture('/Users/Rich/Desktop/makingitup.mov')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

// Prepare output - mp4
videoWriter = cv2.VideoWriter('/Users/Rich/Desktop/testvideo.mp4', cv2.VideoWriter_fourcc('X','2','6','4'),fps,size)

// Read from input, write to output
success, frame = videoCapture.read()
while success:
  videoWriter.write(frame)
  success, frame = videoCapture.read()

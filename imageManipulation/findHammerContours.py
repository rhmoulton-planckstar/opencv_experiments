import cv2, numpy as np

img = cv2.pyrDown(cv2.imread("/Users/Rich/hammer.jpg", cv2.IMREAD_UNCHANGED))

ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# For each contour, we can find and draw the bounding box, minimum enclosing rectangle, and minimum enclosing circle
for c in contours:
  # Find bounding box coords
  x, y, w, h = cv2.boundingRect(c)
  cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

  # Find minimum area
  rect = cv2.minAreaRect(c)

  # Calculate coords of the minimum area rectangle
  box = cv2.boxPoints(rect)
  
  # Normalize coords to integers
  box = np.int0(box)

  # Draw contours
  cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

  # Calculate center and radius of minimum enclosing circle
  (x, y), radius = cv2.minEnclosingCircle(c)
 
  # Cast to integers
  center = (int(x), int(y))
  radius = int(radius)
  
  # Draw the circle
  img = cv2.circle(img, center, radius, (0, 255, 0), 2)

  # Draw the contours and show the image
  cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
  cv2.imshow("contours", img)

  cv2.waitKey()
  cv2.destroyAllWindows()

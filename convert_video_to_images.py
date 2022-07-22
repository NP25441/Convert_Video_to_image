import cv2

vidcap = cv2.VideoCapture('Video-1.mp4')
success, image = vidcap.read()
count = 1
while success:
  cv2.imwrite("img\image_%d.jpg" % count, image)    
  success, image = vidcap.read()
  print('Saved image ', count)
  count += 1
from cv2 import *
import numpy as np
from skimage import filters, feature, io, img_as_ubyte
from skimage.color import rgb2gray

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
namedWindow("cam-test",CV_WINDOW_AUTOSIZE)

loop = True

while loop:
	s, img = cam.read()
	print img.shape

	gray = rgb2gray(img)

	#out = filters.sobel(gray)
	out = feature.canny(gray, 0.5)

	cv_image = img_as_ubyte(out)

	#print out.shape

	#io.imshow(out)
	#io.show()

	imshow("cam-test",cv_image)
	k = waitKey(30)
	print k
	if k == 120:
		# 120 is key 'x' to quit program
		loop = False

print "Closing window..."
destroyWindow("cam-test")

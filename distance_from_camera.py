# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2
def distance_main(path):
	def find_marker(image):
		# convert the image to grayscale, blur it, and detect edges
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (5, 5), 0)
		edged = cv2.Canny(gray, 35, 125)
		# find the contours in the edged image and keep the largest one;
		# we'll assume that this is our piece of paper in the image
		cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		c = max(cnts, key = cv2.contourArea)
		# compute the bounding box of the of the paper region and return it
		return cv2.minAreaRect(c)
		# initialize the known distance from the camera to the object, which
		# in this case is 24 inches
	def distance_to_camera(knownWidth,focalLength,perWidth):
		# compute and return the distance from the maker to the camera
		return (knownWidth * focalLength) / perWidth
	KNOWN_DISTANCE = 17.7
	# initialize the known object width, which in this case, the piece of
	# paper is 12 inches wide
	KNOWN_WIDTH = 8.2
	# load the furst image that contains an object that is KNOWN TO BE 2 feet
	# from our camera, then find the paper marker in the image, and initialize
	# the focal length
	image = cv2.imread("2ft1.jpg")	

	marker = find_marker(image)
	focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
	print(focalLength)
	#for imagePath in sorted(paths.list_images("images")):
	# load the image, find the marker in the image, then compute the
	# distance to the marker from the camera
	imagePath=path
	print(type(path))
	image = cv2.imread(imagePath)
	marker = find_marker(image)
	inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
	return inches
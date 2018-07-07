import cv2
 
class ShapeDetector:
	def __init__(self):
		pass
 
	def detect(self, contour):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		perimeter = cv2.arcLength(contour, True)
		approximate_vertices = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
		approximate_num_vertices = len(approximate_vertices)

		# if the shape is a triangle, it will have 3 vertices
		if approximate_num_vertices == 3:
			shape = "triangle"
 
		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif approximate_num_vertices == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approximate_vertices)
			aspect_ratio = w / float(h)
 
			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			is_square = aspect_ratio >= 0.95 and aspect_ratio <= 1.05
			if is_square:
				shape = "square"
			else:
				shape = "rectangle"
 
		# if the shape is a pentagon, it will have 5 vertices
		elif approximate_num_vertices == 5:
			shape = "pentagon"
 
		# otherwise, we assume the shape is a circle
		else:
			shape = "circle"
 
		# return the name of the shape
		return shape


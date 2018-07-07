import shape_detector as sd
import image_utils as ic
import imutils
import os
import cv2


# Write clean image to disk
image_cleaner = ic.ImageCleaner()
image_path = 'kill-feed-vertical.png'
blue = image_cleaner.find_color(image_path,(103, 198, 218), 50)
red = image_cleaner.find_color(image_path,(225, 40, 50), 50)

#Amplify the red because it's too dark
amped_red = image_cleaner.amplify(image_path, red, 'red')
amped_red_image = image_cleaner.save_array_to_disk(amped_red, 'amped_red')
amped_blue = image_cleaner.amplify(amped_red_image, blue, 'blue')
amped_blue_image = image_cleaner.save_array_to_disk(amped_blue, 'amped_blue')


# Blackout everything except read and blue
both = red + blue
both_array =  image_cleaner.blackout(amped_blue_image, both)
blacked_image_path = image_cleaner.save_array_to_disk(both_array, 'blacked')

#Horizontal crop
cropped_array = image_cleaner.horizontal_crop(blacked_image_path)
image_cleaner.save_array_to_disk(cropped_array, 'cropped')
# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
# image = cv2.imread(clean_image_path)
# resized = imutils.resize(image, width=300)
# ratio = image.shape[0] / float(resized.shape[0])


# # convert the resized image to grayscale, blur it slightly,
# # and threshold it
# gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 200)
# thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# image_cleaner.save_cv2_to_disk(gray, 'gray')
# image_cleaner.save_cv2_to_disk(blurred, 'blurred')
# image_cleaner.save_cv2_to_disk(thresh, 'thresh')
# # find contours in the thresholded image and initialize the
# # shape detector
# contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# if imutils.is_cv2():
# 	contours = contours[0] 
# else:
#  contours = contours[1] 

# shape_detector = sd.ShapeDetector()

# # loop over the contours
# for contour in contours:
# 	# compute the center of the contour, then detect the name of the
# 	# shape using only the contour
# 	# M = cv2.moments(contour)
# 	# cX = int((M["m10"] / M["m00"]) * ratio)
# 	# cY = int((M["m01"] / M["m00"]) * ratio)
# 	shape = shape_detector.detect(contour)
 
# 	# multiply the contour (x, y)-coordinates by the resize ratio,
# 	# then draw the contours and the name of the shape on the image
# 	contour = contour.astype("float")
# 	contour *= ratio
# 	contour = contour.astype("int")
# 	cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
# 	#cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
# 	#	0.5, (255, 255, 255), 2)
 
# # show the output image
# image_cleaner.save_cv2_to_disk(image, 'result')
from PIL import Image, ImageFilter
import numpy as np
import cv2

class ImageCleaner(object):
	"""docstring for ImageCleaner"""
	
	def __init__(self):
		super(ImageCleaner, self).__init__()
		self.count = 0
		self.colormap = {'red':[255,0,0,255],
						 'green':[0,255,0,255],
						 'blue':[0,0,255,255],
						 'black':[0,0,0,255],
						 'white':[255,255,255,255]
					}

	def get_rgb_array(self, image_path):
		image = Image.open(image_path)
		image_rgb = image.convert('RGBA')
		data = np.array(image_rgb)
		return data

	def find_color(self, image_path, rgb, margin):
		data = self.get_rgb_array(image_path)
		red, green, blue, alpha = data.T
		match_area = (red > rgb[0] - margin ) & (red < rgb[0] + margin) \
					  & (green > rgb[1] - margin ) & (green < rgb[1] + margin) \
					  & (blue > rgb[2] - margin ) & (blue < rgb[2] + margin) 
		return match_area

	def amplify(self, image_path, preserve_area, color):
		data = self.get_rgb_array(image_path)
		data[..., :][preserve_area.T] = self.colormap[color]
		return data

	def blackout(self, image_path, preserve_area):
		data = self.get_rgb_array(image_path)
		blackout_area = np.invert(preserve_area)
		data[..., :][blackout_area.T] = self.colormap['white']
		return data
	
	def horizontal_crop(self, image_path):
		data = self.get_rgb_array(image_path)
		print("Shape Before:", data.shape)
		blue = self.colormap['blue']
		red = self.colormap['red']
		percent_blue = (data == blue).mean(axis=(0,2))
		percent_red = (data == red).mean(axis=(0,2))
		minimum_percent = 0.95
		relevant = data[:,
						np.where(percent_blue > minimum_percent)[0].min() : 
						np.where(percent_red > minimum_percent)[0].max(), :
						]
		#print(relevant[0])
		print("Shape After:",relevant.shape)
		return relevant

	def save_array_to_disk(self, array, filename):
		image = Image.fromarray(array)
		step_number = str(self.count).zfill(2)
		filepath = f'images/{step_number}_{filename}.png'
		image.save(filepath)
		self.count += 1
		return filepath

	def save_cv2_to_disk(self, cv2_object, filename):
		step_number = str(self.count).zfill(2)
		filepath = f'images/{step_number}_{filename}.png'
		cv2.imwrite(filepath, cv2_object)
		self.count += 1
		return filepath

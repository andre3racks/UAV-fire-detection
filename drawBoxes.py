# Based off of the work done by Mark Jay: https://youtu.be/Fwcbov4AzQo

import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
# from generate_xml import write_xml

# globals
image  = None
# list of the bottom right mousclick locations from the images
bottomRightMouseClicks = [] 
# list of the top left mousclick locations from the images
topLeftMouseClicks = []
# list of the objects found in an image, i.e. fires found
objectsInImage = []

# constants
imageFolder = 'images' # where the images are
saveDirectory = 'annotations' # where the annotations are saved
obj = 'fire' # the object we're looking for

if __name__ == '__main__':

	# iterate through all the images in the folder
	for n, file in enumerate(os.scandir(imageFolder)):

		# read in the image
		image = file
		figure, axis = plt.subplots(1)
		tempImage = cv2.imread(file.path) 

		# convert colors since cv2 and matplot lib have different color schemes
		tempImage = cv2.cvtColor(tempImage, cv2.COLOR_BGR2RGB)

		# show the images
		axis.imshow(tempImage) 
		plt.show()

# Based off of the work done by Mark Jay: https://youtu.be/Fwcbov4AzQo

import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generateXML import writeXML

# globals
image  = None
# list of the bottom right mousclick locations from the images
bottomRightMouseClicks = [] 
# list of the top left mousclick locations from the images
topLeftMouseClicks = []
# list of the objects found in an image, i.e. fires found
objectsInImage = []

# constants
imageFolder = 'images/kaggle_fire/fire_images/1_50' # where the images are
saveDirectory = 'annotations' # where the annotations are saved
obj = 'fire' # the object we're looking for

# activate the toggle selector recursively
def toggleSelector(event):
	toggleSelector.RS.set_active(True)

# callback function that gets called on each click
def clickCallback(click, release):

	# reference the global lists, so that we can modify them
	global topLeftMouseClicks
	global bottomRightMouseClicks

	# append the click and release data 
	# note: this assumes that we start by clicking from the top left
	topLeftMouseClicks.append((int(click.xdata), int(click.ydata))) 
	bottomRightMouseClicks.append((int(release.xdata), int(release.ydata)))
	objectsInImage.append(obj)

# callback that will happen when we press the 'q' key
def keyPressCallback(event):

	# reference the global lists, so that we can use them in callback
	global objectsInImage
	global topLeftMouseClicks
	global bottomRightMouseClicks
	global image

	# if the 'q' key was hit
	if event.key == 'q':

		writeXML(
			imageFolder,
		 	image,
		 	objectsInImage,
		 	topLeftMouseClicks,
		 	bottomRightMouseClicks,
		 	saveDirectory
		 )

		# clear the data
		image = None
		topLeftMouseClicks = []
		bottomRightMouseClicks = []

		# close the plot
		plt.close()


if __name__ == '__main__':

	# iterate through all the images in the folder
	for n, file in enumerate(os.scandir(imageFolder)):

		# read in the image
		image = file
		figure, axis = plt.subplots(1)
		tempImage = cv2.imread(file.path) 

		# convert colors since cv2 and matplot lib have different color schemes
		tempImage = cv2.cvtColor(tempImage, cv2.COLOR_BGR2RGB)



		# setup the rectangle selector
		toggleSelector.RS = RectangleSelector(
			axis,
			clickCallback,
			drawtype = 'box',
			useblit = True,
			button = [1], # 1 means left mouse click
			minspanx = 5, # value reccomended by matplotlib site
			minspany = 5, # value reccomended by matplotlib site
			spancoords = 'pixels',
			interactive = True
		)

		#connect the events to the toggleSelector and the keyPress callbacks
		boundingBox = plt.connect('key_press_event', toggleSelector)
		keyPress = plt.connect('key_press_event', keyPressCallback)

		# show the image
		axis.imshow(tempImage)
		plt.show()

# Based off of the work done by Mark Jay: https://youtu.be/2XznLUgj1mg

import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET

def writeXML(folder, image, objectsInImage, topLeftMouseClicks, bottomRightMouseClicks, saveDirectory):
	
	# make the save directory, if it doesn't already exist
	if not os.path.isdir(saveDirectory):
		os.mkdir(saveDirectory)

	# read in the image data
	tempImage = cv2.imread(image.path)
	height, width, depth = tempImage.shape

	# create the highest level tag and name it 'annotation'
	annotation = ET.element('annotation')

	# create a folder sublabel tag, and the value to folder
	ET.SubElement(annotation, 'folder').text = folder

	# create a filename sublabel tag, and set the value to the file's name
	ET.SubElement(annotation, 'filename').text = image.name

	# create a segmented sublabel tag, and set the value to 0
	ET.SubElement(annotation, 'segmented').text = '0'

	# create a size subelement with width, height and depth sublabels
	size = ET.SubElement(annotation, 'size')
	ET.SubElement(size, 'width').text = str(width)
	ET.SubElement(size, 'height').text = str(height)
	ET.SubElement(size, 'depth').text = str(depth)

	# iterate through a list of tuples of the objects data
	for object, topLeft, bottomRight in zip(objectsInImage, topLeftMouseClicks, bottomRightMouseClicks):
		
		# create an object sublabel
		objectElement = ET.SubElement(annotation, 'object')

		# create and set the subelements under object
		ET.SubElement(objectElement, 'name').text = object
		# the pose value is unspecified, as we don't care which way the object is facing at the moment
		ET.SubElement(objectElement, 'pose').text = 'Unspecified'
		# the truncated value is set to 0, because we don't care if the fire is blocked at the moment
		ET.SubElement(objectElement, 'truncated').text = '0'
		# as above
		ET.SubElement(objectElement, 'difficult').text = '0'

		# create a bounding box sublabel and set the coordinates
		boundingBox = ET.SubElement(objectElement, 'bndbox')
		# set the xmin coordinate to the first value in the top left tuple
		ET.SubElement(boundingBox, 'xmin').text = str(topLeft[0])
		# set the ymin coordinate to the second value in the top left tuple
		ET.SubElement(boundingBox, 'ymin').text = str(topLeft[1])
		# set the xmax coordinate to the first value in the bottom right
		ET.SubElement(boundingBox, 'xmax').text = str(bottomRight[0])
		# set the ymax coordinate to the second value in the bottom right tuple
		ET.SubElement(boundingBox, 'ymax').text = str(bottomRight[1])

	# get the root level data of the XML tree
	xmlString = ET.tostring(annotation)
	root = etree.fromstring(xmlString)

	# format the data with pretty print
	xmlString = etree.tostring(root, pretty_print=True)










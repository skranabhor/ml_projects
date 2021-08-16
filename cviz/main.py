

from __future__ import print_function
import cv2

image_path = '/Users/shounakranabhor/Desktop/marsrover.png'
image = cv2.imread(image_path)
print('Dimensions of the image: ', image.ndim)
print("Image height: ", format(image.shape[0]))
print("Image width: ", format(image.shape[1]))
print("Image channels: ", format(image.shape[2]))
print("Size of the image array: ", image.size)
cv2.imshow("My Image", image)
cv2.waitKey(0)
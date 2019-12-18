
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

def load(path=None):
	if path=="none":
		image="none"
	else:
		image=cv2.imread(path)
	#print("in")
	return image

def main(img_list):
	# img_list=[]
	# ctr=0
	# for i in range(4):
	# 	path=raw_input("Enter path to image "+str(i))
	# 	print(path)
	# 	img=load(path)
	# 	if img=="none":
	# 		ctr+=1
	# 	else:
	# 		#cv2.imshow('image', img)
	# 		img_list.append(img)
	print(len(img_list))
	stitcher=cv2.Stitcher_create()
	(status, stitched)=stitcher.stitch(img_list)
	cv2.imshow('stitched', stitched)
	return stitched
	if status==0:
		cv2.imshow('stitched', stitched)
		cv2.waitKey(0)
	
if __name__ == "__main__":
	main()


# im=cv2.imread('images/scottsdale/IMG_1786-2.jpg')
# cv2.imshow('image', im)


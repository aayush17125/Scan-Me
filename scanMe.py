import numpy as np
import cv2

#Converting colot image to gray
def color2gray(img):
	img1 = img[:,:,0] #blue channel
	img2 = img[:,:,1] #green channel
	img3 = img[:,:,2] #red channel

	# cv2.imshow("BW1",img1)
	# cv2.imshow("BW2",img2)
	# cv2.imshow("BW3",img3)
	img = (img1*0.11)+(img2*0.59)+(0.3*img3)
	img = img.astype(np.uint8)
	return img

#using openCV gaussian blur
def gaussianBlur(img,r=(5,5)):
	blurred=cv2.GaussianBlur(img,r,0)  #(5,5) is the kernel size and 0 is sigma that determines the amount of blur
	return blurred


#importing image
image = cv2.imread("test_img.jpg")

#resize to 1/3rd of original size so as to fit in screen :p
image=cv2.resize(image,(1088,816))

#make a copy
img = image.copy()

#show original image
cv2.imshow("Original",image)

#using and showing the openCV Color to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray cv2",gray)
	
#using and showing the self-implemented Color to Gray
img = color2gray(img)
cv2.imshow("gray mine",img)

#using gaussian blur openCV
blur = gaussianBlur(img,r=(3,3))
cv2.imshow("Gaussian Blur",blur)




cv2.waitKey(0)
cv2.destroyAllWindows()
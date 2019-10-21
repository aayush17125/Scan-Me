import numpy as np
import cv2
from skimage.filters import threshold_local
import imutils


#Converting color image to gray
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

#using openCV canny edge detection
def cannyEdge(img,minT,maxT):
	edge=cv2.Canny(img,minT,maxT)  # minT and maxT are minimum and maximum threshold for edge detection
	return edge 

#Perspective transform
def transformFourPoints(image, pts):   # reference : https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/

	rect = np.zeros((4, 2), dtype="float32")

	s = pts.sum(axis=1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]


	diff = np.diff(pts, axis=1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	(tl, tr, br, bl) = rect


	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))


	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))


	dst = np.array([[0, 0],	[maxWidth - 1, 0],	[maxWidth - 1, maxHeight - 1],	[0, maxHeight - 1]], dtype="float32")


	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

	return warped



if __name__=="__main__":

	#importing image
	image = cv2.imread("test.jpeg")
	ratio = image.shape[0] / 500.0
	orig = image.copy()
	#resize to 1/3rd of original size so as to fit in screen :p
	image= imutils.resize(image,height=500)

	#make a copy
	img = image.copy()

	#using and showing the self-implemented Color to Gray
	img = color2gray(img)


	#using gaussian blur openCV
	blur = gaussianBlur(img,r=(5,5))


	#using Canny edge detection openCV
	edge = cannyEdge(blur,minT=50,maxT=100)


	cnts = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0]
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
	for c in cnts:
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		if len(approx) == 4:
			screenCnt = approx
			break
	# print("Finding contours of paper...")                        #Uncomment to see the contours of the input. Also uncomment the line with Outline in the View All images section
	# cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
	print("Applying perspective transform...")
	warped = transformFourPoints(orig, screenCnt.reshape(4, 2) * ratio)

	warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
	T = threshold_local(warped, 11, offset = 10, method = "gaussian")
	warped = (warped > T).astype("uint8") * 255

	#view all images
	
	cv2.imshow("Scanned", imutils.resize(warped, height = 650))
	# cv2.imshow("Outline", image)
	cv2.imshow("Edge detection",edge)
	cv2.imshow("Gaussian Blur",blur)
	cv2.imshow("gray",img)
	cv2.imshow("Original",image)
	


	cv2.waitKey(0)
	cv2.destroyAllWindows()
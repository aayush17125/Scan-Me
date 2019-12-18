import numpy as np
import cv2
from skimage.filters import threshold_local
import imutils
from matplotlib import pyplot as plt
# from pyimagesearch.transform import four_point_transform
img=0
img1=0
img2=0
img3=0
img4=0
img5=0
img6=0
def changeimg(path):
	global img1,img2,img3,img4,img5,img6
	image = cv2.imread(path)
	ratio = image.shape[0]/500.0
	orig = image.copy()
	#resize to 1/3rd of original size so as to fit in screen :p
	image= imutils.resize(image,height=500)

	#make a copy
	img = image.copy()

	#using and showing the self-implemented Color to Gray
	img = color2gray(img)


	#using gaussian blur openCV
	blur = gaussianBlur(img,r=(5,5))
	flag, thresh1 = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

	# using Canny edge detection openCV
	edge = cannyEdge(thresh1,minT=50,maxT=100)
	try:
		cnts = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0]
		# print(cnts[0])
		cnts = sorted(cnts, key = cv2.contourArea, reverse = True)
		cnts = cnts[:5]
		for c in cnts:
			perim = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.02 * perim, True)
			if len(approx) == 4:
				screenCnt = approx
				break
		print("Finding contours of paper...")                        #Uncomment to see the contours of the input. Also uncomment the line with Outline in the View All images section
		cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
		print("Applying perspective transform...")
		warped = transformFourPoints(orig, screenCnt.reshape(4, 2) * ratio)
		warped = color2gray(warped)
		# T = threshold_local(warped, 9, offset = 12, method = "gaussian")
		# warped = (warped > T).astype("uint8") * 255
		ret2,thresh = cv2.threshold(warped,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		denoised = cv2.fastNlMeansDenoising(thresh, 11, 31, 11)
		#view all images
		img6 = imutils.resize(denoised, height = 650)
		print(img6.shape,'--'*50)
		img5 =  image
		img4 = edge
		img3 = imutils.resize(thresh1,height=650)
		img2 = blur
		img1 = img
	except Exception as e:
		print('Error: ', e)
		img5=cv2.imread("C:\\Users\\Sherlock\\Desktop\\Work\\5th Sem\\DIP\\Project\\Scan-Me-master\\error.jpg")



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
	kernel = cv2.getGaussianKernel(ksize=5,sigma=0)
	print(kernel)
	blurred=cv2.GaussianBlur(img,r,0)  #(5,5) is the kernel size and 0 is sigma that determines the amount of blur
	print(blurred)
	#self blur not working
	filt = np.ones(r)
	self_blurred = cv2.filter2D(img,-1,filt)
	print(self_blurred)
	

	return blurred

#using openCV canny edge detection
def cannyEdge(img,minT=75,maxT=200):
	edge=cv2.Canny(img,minT,maxT)  # minT and maxT are minimum and maximum threshold for edge detection
	print(type(edge))
	return edge 

#Perspective transform
def transformFourPoints(img,pts):   # reference : https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/

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
	warped = cv2.warpPerspective(img, M, (maxWidth, maxHeight))

	return warped



if __name__=="__main__":

	#importing image
	image = cv2.imread("page.jpg")
	ratio = image.shape[0]/500.0
	orig = image.copy()
	#resize to 1/3rd of original size so as to fit in screen :p
	image= imutils.resize(image,height=500)

	#make a copy
	img = image.copy()

	#using and showing the self-implemented Color to Gray
	img = color2gray(img)


	#using gaussian blur openCV
	blur = gaussianBlur(img,r=(5,5))
	flag, thresh1 = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

	# using Canny edge detection openCV
	edge = cannyEdge(thresh1,minT=50,maxT=100)
	cnts = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0]
	# print(cnts[0])
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)
	cnts = cnts[:5]
	for c in cnts:
		perim = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * perim, True)
		if len(approx) == 4:
			screenCnt = approx
			break
	print("Finding contours of paper...")                        #Uncomment to see the contours of the input. Also uncomment the line with Outline in the View All images section
	cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)


	
	


	print("Applying perspective transform...")
	warped = transformFourPoints(orig, screenCnt.reshape(4, 2) * ratio)

	warped = color2gray(warped)
	# T = threshold_local(warped, 9, offset = 12, method = "gaussian")
	# warped = (warped > T).astype("uint8") * 255
	ret2,thresh = cv2.threshold(warped,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	denoised = cv2.fastNlMeansDenoising(thresh, 11, 31, 11)
	#view all images
	
	cv2.imshow("Scanned", imutils.resize(denoised, height = 1000))
	cv2.imshow("Outline", image)
	cv2.imshow("Edge detection",edge)
	cv2.imshow("threshold", imutils.resize(thresh1,height=650))
	cv2.imshow("Gaussian Blur",blur)
	cv2.imshow("gray",img)
	cv2.imshow("Original",imutils.resize(orig,height=650))
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()
import numpy as np
import cv2

image = cv2.imread("test_img.jpg")
image=cv2.resize(image,(1088,816))
img = image.copy()
print(type(image[0,0,0]))
cv2.imshow("",image)

print(type(img),img.shape)

img1 = img[:,:,0] #blue channel
img2 = img[:,:,1] #green channel
img3 = img[:,:,2] #red channel

# cv2.imshow("BW1",img1)
# cv2.imshow("BW2",img2)
# cv2.imshow("BW3",img3)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray cv2",gray)
img = (img1*0.11)+(img2*0.59)+(0.3*img3)
img = img.astype(np.uint8)
print(type(img[0,0]))
print(type(img),img.shape,img)
cv2.imshow("gray mine",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
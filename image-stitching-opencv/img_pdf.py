import img2pdf 
from PIL import Image 
import os 
  
# # storing image path 
# img_path = "images/page/1.jpg"
  
# # storing pdf path 
# pdf_path = "file.pdf"
  
# # opening image 
# image = Image.open(img_path) 
  
# # converting into chunks using img2pdf 
# pdf_bytes = img2pdf.convert(image.filename) 
  
# # opening or creating pdf file 
# file = open(pdf_path, "wb") 
  
# # writing pdf files with chunks 
# file.write(pdf_bytes) 
  
# # closing image file 
# image.close() 
  
# # closing pdf file 
# file.close() 


def conv_end(img, pdf):
	img=Image.open(img)
	file_pdf=img2pdf.convert(img.filename)
	#print("ehy")
	to_return=open(pdf, "wb")
	to_return.write(file_pdf)
	img.close()


def main(): 
	img="images/page/1.jpg"
	pdf="file.pdf"
	conv_end(img, pdf)
if __name__ == "__main__":
	main()

  
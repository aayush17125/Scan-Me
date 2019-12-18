import tkinter as tk 
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import scanMe as sm
import cv2
import imutils
import try_stitch as st
import img2pdf 
from PIL import Image 
import os 


	# ###For loading cv2 images:
	# image = cv2.imread("test.jpg")
	# 	b,g,r = cv2.split(image)
	# 	image = cv2.merge((r,g,b))
	# 	print(image.shape)
	# 	im = Image.fromarray(image)
	# 	imgtk = ImageTk.PhotoImage(image=im) 



	# 	# img = ImageTk.PhotoImage(Image.open(imgtk))
	# 	panel = Label(inimgfr, image = imgtk)
	# 	panel.image=imgtk
	# 	panel.place(relheight=1,relwidth=1)
curr_img=0
def togrey():
	global curr_img
	image = sm.img1
	curr_img=sm.img1
	print("hello",image)
	# b,g,r = cv2.split(image)
	# image = cv2.merge((r,g,b))
	# print(image.shape)
	im = Image.fromarray(image)
	imgtk = ImageTk.PhotoImage(image=im) 
	# img = ImageTk.PhotoImage(Image.open(imgtk))
	panel = Label(outimgfr, image = imgtk)
	panel.image=imgtk
	panel.place(relheight=1,relwidth=1)


def gaus():
	global curr_img
	image = sm.img2
	curr_img=sm.img2
	print("hello",image)
	# b,g,r = cv2.split(image)
	# image = cv2.merge((r,g,b))
	# print(image.shape)
	im = Image.fromarray(image)
	imgtk = ImageTk.PhotoImage(image=im) 
	# img = ImageTk.PhotoImage(Image.open(imgtk))
	panel = Label(outimgfr, image = imgtk)
	panel.image=imgtk
	panel.place(relheight=1,relwidth=1)


def tocann():
	global curr_img
	image = sm.img4
	curr_img=sm.img3
	print("hello",image)
	# b,g,r = cv2.split(image)
	# image = cv2.merge((r,g,b))
	# print(image.shape)
	im = Image.fromarray(image)
	imgtk = ImageTk.PhotoImage(image=im) 
	# img = ImageTk.PhotoImage(Image.open(imgtk))
	panel = Label(outimgfr, image = imgtk)
	panel.image=imgtk
	panel.place(relheight=1,relwidth=1)


def tothresh():
	global curr_img
	image = sm.img3
	curr_img=sm.img4
	print("hello",image)
	# b,g,r = cv2.split(image)
	# image = cv2.merge((r,g,b))
	# print(image.shape)
	im = Image.fromarray(image)
	imgtk = ImageTk.PhotoImage(image=im) 
	# img = ImageTk.PhotoImage(Image.open(imgtk))
	panel = Label(outimgfr, image = imgtk)
	panel.image=imgtk
	panel.place(relheight=1,relwidth=1)

def toout():
	global curr_img
	image = sm.img5
	curr_img=sm.img5
	print("hello",image)
	b,g,r = cv2.split(image)
	image = cv2.merge((r,g,b))
	print(image.shape)
	# image=imutils.resize(image,height=500)
	im = Image.fromarray(image)
	imgtk = ImageTk.PhotoImage(image=im) 
	# img = ImageTk.PhotoImage(Image.open(imgtk))
	panel = Label(outimgfr, image = imgtk)
	panel.image=imgtk
	panel.place(relheight=1,relwidth=1)

def finalout():
	global curr_img
	image = sm.img6
	curr_img=sm.img6
	print("hello",image)
	# b,g,r = cv2.split(image)
	# image = cv2.merge((r,g,b))
	# print(image.shape)
	im = Image.fromarray(image)
	imgtk = ImageTk.PhotoImage(image=im) 
	# img = ImageTk.PhotoImage(Image.open(imgtk))
	panel = Label(outimgfr, image = imgtk)
	panel.image=imgtk
	panel.place(relheight=1,relwidth=1)


def topdf():
	global curr_img,i
	# curr_img = sm.img7
	#-----------------------------------------------------------------------------Arjun change this to your path------------------------------------------------
	#-----------------------------------------------------------------------------Arjun change this to your path------------------------------------------------
	#-----------------------------------------------------------------------------Arjun change this to your path------------------------------------------------
	#-----------------------------------------------------------------------------Arjun change this to your path------------------------------------------------
	os.chdir('./SavedImages') 
	#-----------------------------------------------------------------------------Arjun change this to your path------------------------------------------------
	#-----------------------------------------------------------------------------Arjun change this to your path------------------------------------------------
	#-----------------------------------------------------------------------------Arjun change this to your path------------------------------------------------
	#-----------------------------------------------------------------------------Arjun change this to your path------------------------------------------------
	cv2.imwrite("out"+str(i)+".jpg", curr_img) 
	img=Image.open("./out"+str(i)+".jpg")
	# cv2.imshow("got",img)
	file_pdf=img2pdf.convert(img.filename)
	#print("ehy")
	to_return=open("pdf"+str(i)+".pdf", "wb")
	to_return.write(file_pdf)
	img.close()
	i=i+1


def stitchit():
	global filename,curr_img
	img_list=[]
	for i in filename:
		img=cv2.imread(i)
		img_list.append(img)
	image=st.main(img_list)
	# image = sm.img6
	curr_img=image
	print("hello",image)
	# b,g,r = cv2.split(image)
	# image = cv2.merge((r,g,b))
	# print(image.shape)
	im = Image.fromarray(image)
	imgtk = ImageTk.PhotoImage(image=im) 
	# img = ImageTk.PhotoImage(Image.open(imgtk))
	panel = Label(outimgfr, image = imgtk)
	panel.image=imgtk
	panel.place(relheight=1,relwidth=1)







filename=[]
def addImg():
	global filename
	filename=filedialog.askopenfilenames(initialdir="./",title="Select File",filetypes = (("jpg files","*.jpg"),("jpeg files","*.jpeg"),("all files","*.*")))
	print(filename[0])
	# print(fli)
	sm.changeimg(filename[0])
	image = cv2.imread(filename[0])
	ratio = image.shape[0]/500.0
	#resize to 1/3rd of original size so as to fit in screen :p
	image= imutils.resize(image,height=500)
	b,g,r = cv2.split(image)
	image = cv2.merge((r,g,b))
	print(image.shape)
	im = Image.fromarray(image)
	imgtk = ImageTk.PhotoImage(image=im) 



	# img = ImageTk.PhotoImage(Image.open(imgtk))
	panel = Label(inimgfr, image = imgtk)
	panel.image=imgtk
	panel.place(relheight=1,relwidth=1)

	# img = ImageTk.PhotoImage(Image.open(filename))
	# panel = Label(inimgfr, image = img)
	# panel.image=img
	# panel.place(relheight=0.9,relwidth=0.9)

# def addImg():
# 	filename=filedialog.askopenfilename(initialdir="C:\\Users\\Sherlock\\Desktop\\Work\\5th Sem\\DIP\\Project\\",title="Select File",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# 	print(filename)
	
# 	img = ImageTk.PhotoImage(Image.open(filename))
# 	panel = Label(inimgfr, image = img)
# 	panel.image=img
# 	panel.place(relheight=1,relwidth=1)	

root = tk.Tk() 

root.title('CamScanner') 
i=0
canvas=tk.Canvas(root,height=800,width=1000,bg="#030301")
canvas.pack()
canvas.create_text(550,50,text="CamScammer",fill="#FFFFF3",font="TimesNewRoman 40 bold")
inimgfr=tk.Frame(canvas,bg="#FFFFF3")
inimgfr.place(width=400,height=500,relx=0.1,rely=0.1)

outimgfr=tk.Frame(canvas,bg="#FFFFF3")
outimgfr.place(x=450,width=400,height=500,relx=0.1,rely=0.1)

buttframe=tk.Frame(canvas,bg="#030301",padx=40)
buttframe.place(y=600,x=175,width=900,relheight=0.2)

butt_font="none 9 bold"
butt_w=10
upbutton = tk.Button(buttframe, text='Upload', height=2,width=butt_w, command=addImg,bg="#FF4365",font=butt_font) 
upbutton.grid(row=2, column=0,pady=25)

f1 = tk.Button(buttframe, text='Greyscale',height=2, width=butt_w, command=togrey,bg="#00D9C0",font=butt_font) 
f1.grid(row=2, column=1,padx=5)

f2 = tk.Button(buttframe, text='Gaussian\n Smoothing',height=2, width=butt_w, command=gaus,bg="#00D9C0",font=butt_font) 
f2.grid(row=2, column=2,padx=5)

f4 = tk.Button(buttframe, text='Thresholding',height=2, width=butt_w, command=tothresh,bg="#00D9C0",font=butt_font) 
f4.grid(row=2, column=3,padx=5)

f3 = tk.Button(buttframe, text='Canny Edge',height=2, width=butt_w, command=tocann,bg="#00D9C0",font=butt_font) 
f3.grid(row=2, column=4,padx=5)

f5 = tk.Button(buttframe, text='Outlines',height=2, width=butt_w, command=toout,bg="#00D9C0",font=butt_font) 
f5.grid(row=2, column=5,padx=5)

f6 = tk.Button(buttframe, text='Perspective\n Transform',height=2, width=butt_w, command=finalout,bg="#00D9C0",font=butt_font) 
f6.grid(row=2, column=6,padx=5)

f7 = tk.Button(buttframe, text='Save as PDF',height=2, width=butt_w, command=topdf,bg="#FF4365",font=butt_font) 
f7.grid(row=3, column=3,padx=0)


f8 = tk.Button(buttframe, text='Stitch Images',height=2, width=butt_w, command=stitchit,bg="#FF4365",font=butt_font) 
f8.grid(row=3, column=4,padx=0)
root.mainloop() 
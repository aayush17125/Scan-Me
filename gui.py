import tkinter as tk 
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import scanMe as sm
import cv2
import imutils

def togrey():
	image = sm.img1
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
	image = sm.img2
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
	image = sm.img3
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
	image = sm.img4
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
	image = sm.img5
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
	image = sm.img6
	print("hello",image)
	im = Image.fromarray(image)
	imgtk = ImageTk.PhotoImage(image=im) 
	panel = Label(outimgfr, image = imgtk)
	panel.image=imgtk
	panel.place(relheight=1,relwidth=1)

def addImg():
	filename=filedialog.askopenfilename(initialdir="C:\\Users\\Sherlock\\Desktop\\Work\\5th Sem\\DIP\\Project\\",title="Select File",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	print(filename)
	sm.changeimg(filename)
	image = cv2.imread(filename)
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


root = tk.Tk() 
root.title('CamScanner') 

canvas=tk.Canvas(root,height=800,width=1000,bg="#030301")
canvas.pack()

inimgfr=tk.Frame(canvas,bg="#FFFFF3")
inimgfr.place(width=400,height=500,relx=0.1,rely=0.1)

outimgfr=tk.Frame(canvas,bg="#FFFFF3")
outimgfr.place(x=450,width=400,height=500,relx=0.1,rely=0.1)

buttframe=tk.Frame(canvas,bg="#030301",padx=40)
buttframe.place(y=600,x=200,width=700,relheight=0.1)

upbutton = tk.Button(buttframe, text='Upload', height=2,width=10, command=addImg,bg="#FF4365",font="none 11 bold") 
upbutton.grid(row=2, column=0,pady=25)

f1 = tk.Button(buttframe, text='Greyscale',height=2, width=10, command=finalout,bg="#00D9C0",font="none 11 bold") 
f1.grid(row=2, column=1,padx=5)

f2 = tk.Button(buttframe, text='Gaussian\n Smoothing',height=2, width=10, command=gaus,bg="#00D9C0",font="none 11 bold") 
f2.grid(row=2, column=2,padx=5)

f3 = tk.Button(buttframe, text='Canny Edge',height=2, width=10, command=tocann,bg="#00D9C0",font="none 11 bold") 
f3.grid(row=2, column=4,padx=5)

f4 = tk.Button(buttframe, text='Thresholding',height=2, width=10, command=tothresh,bg="#00D9C0",font="none 11 bold") 
f4.grid(row=2, column=3,padx=5)

f5 = tk.Button(buttframe, text='Outlines',height=2, width=10, command=finalout,bg="#00D9C0",font="none 11 bold") 
f5.grid(row=2, column=5,padx=5)

# f6 = tk.Button(buttframe, text='Final',height=2, width=10, command=finalout,bg="#27476E",font="none 11 bold") 
# f5.grid(row=3, column=1,padx=5)
root.mainloop() 
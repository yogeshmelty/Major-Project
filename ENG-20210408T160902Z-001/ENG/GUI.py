from tkinter import *
from tkinter import filedialog
import mediator as m
import sys

 
window = Tk()
a = ""
window.title("BLINDSIGHT FOR ENGLISH")

window.geometry('1000x600')

def Font():
	return ('Times New Roman','15')

labelframe1 = LabelFrame(window,text = "File Selection Status",font = Font())

labelframe1.pack()

label1 = Label(labelframe1,width = 150,height =10,font = Font())

label1.pack()

labelframe2 = LabelFrame(window,text = "Path Of Selected File",font = Font())

labelframe2.pack()

label2 = Label(labelframe2,width = 150,height =10,font = Font())
label2.pack()

frame = Frame(window)

frame.pack()

label1.config( text = "No File Selected" )
label2.config( text = "No File Selected" )

def RESET():
	label1.config( text = "No File Selected" )
	label2.config( text = "No File Selected" )

def COmmOnFileSeLecTor():
	filename = filedialog.askopenfilename()
	if filename == "" :
		RESET()
	else :
		label1.config( text = " File Selected " )
		label2.config( text = filename )
	return filename

def open3Dfile() :
	m.text2Braille()
	label1.config(text = "3D BRAILLE IS READY FOR PRINTING")

def AUDIO_SELECTOR():
	filename = COmmOnFileSeLecTor()
	if filename == "" :
		RESET()
	else :
		#print("write code for audio")
		m.filePathName(filename)
		label1.config(text = "CONVERTED AUDIO TO TEXT")
		

def VIDEO_SELECTOR():
	filename = COmmOnFileSeLecTor()
	if filename == "" :
		RESET()
	else :
		m.convertVideo(filename)
		label1.config(text = "CONVERTED VIDEO TO AUDIO")
		

def VOICE_SELECTOR():
	m.record()
	label1.config(text = "CONVERTED VOICE TO TEXT")

def TEXT_SELECTOR():
	filename = COmmOnFileSeLecTor()
	if filename == "" :
		RESET()
	else :
		m.makeSummary(filename)
		label1.config(text = "SUMMARIZED TEXT FILE IS PREPARED")

def IMAGE_SELECTOR():
	filename = COmmOnFileSeLecTor()
	if filename == "" :
		RESET()
	else :
		m.textImage(filename)
		label1.config(text = "CONVERTED IMAGE TO TEXT")
		
def EXIT():
	sys.exit(1)

b2 = Button(frame,text="VIDEO",command = VIDEO_SELECTOR,font = Font());

b2.pack(padx=20,pady=0,side="left")
	
b1 = Button(frame,text="VOICE",command = VOICE_SELECTOR,font = Font());

b1.pack(padx=20,pady=0,side = "left")
	
	
b0 = Button(frame,text="AUDIO",command = AUDIO_SELECTOR,font = Font());

b0.pack(padx=20,pady=0,side = "left")


b3 = Button(frame,text="IMAGE",command = IMAGE_SELECTOR,font = Font());

b3.pack(padx=20,pady=0,side="left")

b4 = Button(frame,text="TEXT",command = TEXT_SELECTOR,font = Font());

b4.pack(padx=20,pady=0,side="left")


b5 = Button(frame,text="3D-FILE",command = open3Dfile,font = Font());

b5.pack(padx=20,pady=0,side="left")

b6 = Button(frame,text="RESET",command = RESET,font = Font());

b6.pack(padx=20,pady=0,side="left")

b7 = Button(frame,text="EXIT",command = EXIT,font = Font());

b7.pack(padx=20,pady=0,side="right")

window.mainloop()

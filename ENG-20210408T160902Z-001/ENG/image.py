import pytesseract as tess
tess.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image

def textFromImage(filename):
	im = Image.open(filename)
	text = tess.image_to_string(im,lang = "eng")
	pathWriteFile = "Output.txt"
	f= open(pathWriteFile,'w',encoding = "UTF-8")
	f.write(str(text))
	f.close()




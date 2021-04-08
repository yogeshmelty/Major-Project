import text2stl as t
print("Imported stl package")
import video as vi
print("Imported video package")
import image as i
print("Imported image package")
import englishText as et
print("Imported english text package")
import convert2Braille as c
print('Imported braille mapping package')
import audio as a
print("Imported audio package")
import voice as v
print("Imported voice package")


def filePathName(x):
	a.filePath(x)
	
def record():
	v.recordVoice()
	


def makeSummary(filename):
	et.run(filename)

def convertVideo(path):
	vi.video_to_audio(path)
	
def textImage(filename):
	i.textFromImage(filename)
	
def text2Braille():
	c.convertFile()
	t.run()
	
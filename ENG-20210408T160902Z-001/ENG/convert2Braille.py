import alphaToBraille as a

def convertFile():
	f = open('InputOutput.txt','r')
	content = f.read()
	f.close()
	content = a.translate(content)
	f = open('Output.txt','w',encoding = 'UTF8')
	f.write(content)
	f.close()
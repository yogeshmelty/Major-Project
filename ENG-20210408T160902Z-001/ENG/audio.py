import tensorflow as tf
import pandas as pd
import numpy as np
from multiprocessing import Pool
import librosa
import os

PATH ='174-84280-0001.flac'


final_text="Text goes here"

def to_path(filename):
    return  filename

SAMPLING_RATE=16000

def saveFile():
    f = open("Input.txt",'w')
    f.write(final_text)
    f.close()
    print('File saved')


def filePath(filename):
    global PATH
    PATH = filename
    run()
	
def run():
	import convert as c
	global final_text
	final_text = c.translate(PATH)
	saveFile()

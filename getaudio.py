import requests
import time
import sys,getopt
import random
from playsound import playsound

def getURL(word):
    url = "http://dict.youdao.com/dictvoice?type=0&audio=" + word
    return url

def readwords(words):
    for word in words:
        playsound(getURL(word))
        time.sleep(0.5)

if __name__=="__main__":
    shuffle = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:s", ["ifile-"])
    except getopt.GetoptError:
        print ('python3 getaudio.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in("-i", "--ifile"):
            words = open(arg).readlines()
        elif opt == '-s':
            shuffle = 1
    if shuffle == 1:
        random.shuffle(words)
    readwords(words)

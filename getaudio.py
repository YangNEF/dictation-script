import requests
import time
from playsound import playsound

def getURL(word):
    url = "http://dict.youdao.com/dictvoice?type=0&audio=" + word
    return url

if __name__=="__main__":
    for line in open("wordlist.txt"):
        word = line
        playsound(getURL(word))
        time.sleep(0.5)
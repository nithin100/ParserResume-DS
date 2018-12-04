import os

import PyPDF2 
#import textract

def getTextFromFile(textPath):
    extension = os.path.splitext(textPath)[-1]
    print(extension)
    if(extension=='.txt'):
        fileHandler = open(textPath,'r')
        print(fileHandler.read())

getTextFromFile('../shared/Data/somefile.txt')

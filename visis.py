import click
import sys
from pyfiglet import Figlet
# import json
import time
import io
import os
from google.cloud import vision
import cv2
import pytesseract
import vivi
from ppii import deepSpell
from decouple import config


# client = config('client')



@click.group()
@click.version_option(version='0.01', prog_name='Visis') 
def main():
    """ Visis """
    pass

# image path
path = "/Volumes/Loopdisk/Visis/Caveats.png"


# Extract text
#@main.command()
#@click.argument('path')
# function for transcribing image content and append words and line
def extract(input):
    """Extract text from Images"""
    image = cv2.imread(input, cv2.IMREAD_COLOR)
    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(image, config=config)
    return text


# def extract(input, engine="pytesseract"):
#     """Extract text from Images"""
#     engines = ['gvision', 'pytesseract']
#     if engine not in engines:
#         raise ValueError("Invalid engine. Expected one of: %s" % engines)
#         if engine is pytesseract:
#             image = cv2.imread(input, cv2.IMREAD_COLOR)
#             config = ('-l eng --oem 1 --psm 3')
#             text = pytesseract.image_to_string(image, config=config)
#             return text
                    #print(lines)
    # else:
    #     from google.cloud import vision
    #     client = vision.ImageAnnotatorClient()
    #     with io.open(input, 'rb') as image_input:
    #         content = image_input.read()
    #         image = vision.types.Image(content=content)
    #         response = client.text_detection(image=image)
    #         return(' '.join([d.description for d in response.text_annotations]))
# x = extract(path, engine="pytesseract")

x = extract(path)
x = extract(path)
x = deepSpell(x, 1)
print(x)


# # def replaceSpecialCharactersWithSpace(filePath):
# #     import re
# #     file_content = []
# #     # filestring = 0
# #     for line in open(filePath, 'r'):
# #         file_content.append(line.strip())
# #         filestring = ' '.join(x for x in file_content)
# #         correctedFile = re.sub('[^a-zA-Z]', ' ', filestring)
# #         return correctedFile

# # def cleantTranscript(transcribedTextDir, cleantTranscribedTextDir):
# #     for transcribedText in os.listdir(transcribedTextDir):
# #             print('----------------------')
# #             print('working for '+str(transcribedText))
# #             print('----------------------')
# #             textPath = os.path.join(transcribedTextDir, transcribedText)
    
# #             content = replaceSpecialCharactersWithSpace(textPath)
    
# #             print('finished removing special characters')
# #             filename = ''.join(transcribedText.split('.')[:-1])
# #             filename = filename+'.txt'
# #             newFilePath = os.path.join(cleantTranscribedTextDir,filename)
# #             print('writing to txt file')
# #             save(newFilePath, content)

        
# # cleantTranscript('transcribed_images', 'clean_transcribed_images/')


# # def writeTranscribedText(transcribedTextDir, correctedTextDir, option):
# #     for transcribedText in os.listdir(transcribedTextDir):
# #         print('----------------------')
# #         print('working for '+str(transcribedText))
# #         print('----------------------')
# #         textPath = os.path.join(transcribedTextDir, transcribedText)
    
# #         content = deepSpell(textPath,option )
            
# #         print('finished correcting')
# #         filename = ''.join(transcribedText.split('.')[:-1])
# #         filename = filename+'.txt'
# #         newFilePath = os.path.join(correctedTextDir,filename)
# #         print('writing to txt file')
# #         save(newFilePath, content)



# # writeTranscribedText('clean_transcribed_images', 'corrected_transcripts_decode/', 1)

# # writeTranscribedText('clean_transcribed_images', 'corrected_transcripts_target', 2)


# vivi.whisper(x)
# sys.exit()


# # save text file function
# def save(filename, contents):
#     fh = open(filename, 'w')  
#     fh.write(contents)  
#     fh.close()



# def save_to_file(x):
# 	timestr = time.strftime("%Y%m%d-%H%M%S")
# 	filename = 'result' + '.txt'
# 	with open(filename, 'w') as f:
# 		 f.write(x)


# # save_to_file(x)

# # Abouts
# @main.command()
# @click.option('--about')
# # STYLED NAME with Figlet
# # """ About Visis """
# def info(about):
#     f = Figlet(font="slant")
#     print(f.renderText("Visis CLI"))



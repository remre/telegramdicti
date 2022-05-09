from googletrans import Translator
import requests
from bs4 import BeautifulSoup as bs
from google.cloud import texttospeech
import re
import pandas


import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/emreb/Documents/projects/secret/projecttelebotapi-cafc88105725.json'


# def translatetext(text,*args):
#     translator = Translator()

#     if args != ():
#         if len(args) == 1:
#             result = translator.translate(text, dest=args[0])
#         if len(args) == 2:
#             result = translator.translate(text, src=args[1], dest=args[0])
#         return result.text
#     else:
#         destlang = text.split('tolang ')[1]
#         maintext = text.split('tolang ')[0]
#         result = translator.translate(maintext,destlang)
#         return result.text, args

# k = translatetext('que tal tolang tr',)
textt = 'que tal tolang tr moi aussi'

distint = textt.split('tolangg ')
try:
    destlang = distint[1]
    maintext = distint[0]   
except:
    spilit = textt.split()
    dest = spilit[-1]
    textlack = " ".join(spilit[:-1])
if len(distint) == 2:   
    print(destlang)
else:
    print(dest), print(textlack)


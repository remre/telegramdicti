import inflect
from bs4 import BeautifulSoup as bs
from googletrans import Translator
from random_word import RandomWords
import numpy as np
import random 
import glob

def number_gen(destlang):
    file_object = open(f'w_seltexts/{destlang}1.txt', 'a',errors='ignore')
    for number in range(1,100):
        p = inflect.engine()
        numberr = p.number_to_words(number)
        translator = Translator()
        translated_t_answer = translator.translate(text=numberr, dest=destlang)
        file_object.write('\n'+translated_t_answer.text)

number_gen('el')
# file = [file.split('\\')[1].split('.')[0] for file in glob.glob("w_seltexts\*.txt")]
# print(file) 


# destlang = 'fr'
# if [destlang != file.split('\\')[1].split('.')[0] for file in glob.glob("w_seltexts\*.txt")]:
#     destlang ='de'
#     # print('file not found')

# else:
#     destlang = destlang

# print(destlang)
# value = [] 
# {value.append(file.split('\\')[1].split('.')[0]) for file in glob.glob("w_seltexts\*.txt")}
# if 'id' in value:
#     print('file not found')
 
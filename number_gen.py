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



def wrong_answers(ttta,destlang='de',hardness=None):
    wrong_answers = []
    value = [] 
    {value.append(file.split('\\')[1].split('.')[0]) for file in glob.glob("w_seltexts\*.txt")} 
    if destlang in value:
        destlang = destlang
        
    else:
        destlang ='de'
    if hardness != None:
        if destlang+str(hardness) in value:
            with open(f'w_seltexts/{destlang}{hardness}.txt', 'r', errors='replace') as f:
                lines = f.readlines()
                print(lines[:4])
        else:
            with open(f'w_seltexts/{destlang}.txt', 'r', errors='replace') as f:
                lines = f.readlines()
    else:
        with open(f'w_seltexts/{destlang}.txt', 'r', errors='replace') as f:
            lines = f.readlines()
    for line in lines:
        if line[:2]==ttta[:2]:
                if len(ttta)+1 >=len(line)>=len(ttta)-1:
                    wrong_answers.append(line.strip())
                else:
                    wrong_answers.append(line.strip()) 
    return random.choices(wrong_answers,k =3)

co = wrong_answers('vingt-trois', 'fr',)
print(co)
# number_gen('el')
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
 
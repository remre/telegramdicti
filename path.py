import inflect
from bs4 import BeautifulSoup as bs
from googletrans import Translator
from random_word import RandomWords
import numpy as np
import random 
import glob

r_word = RandomWords()
true_answer = r_word.get_random_word()
translator = Translator()
translated_t_answer = translator.translate(true_answer, dest='es')
ttta = translated_t_answer.text
d_lang = translated_t_answer.dest
# print(d_lang)
# if [d_lang != file.split('\\')[1].split('.')[0] for file in glob.glob("w_seltexts/*.txt") ]:
#     d_lang = 'de'
# else:
#     d_lang = d_lang
# print([file.split('\\')[1].split('.')[0] for file in glob.glob("w_seltexts/*.txt") ])
print(type(d_lang))
# print(ttta)
# def wrong_answers(ttta,destlang='de',hardness=None):
#     wrong_answers = []
#     if [destlang != file.split('\\')[1].split('.')[0] for file in glob.glob("w_seltexts\*.txt") ]:
#         destlang = 'de'
#     else:
#         destlang = destlang

#     if hardness != None:

#         with open(f'w_seltexts/{destlang}{hardness}.txt', 'r') as f:
#             lines = f.readlines()
#     else:
#         with open(f'w_seltexts/{destlang}.txt', 'r') as f:
#             lines = f.readlines()
#     for line in lines:
#         if line[:2]==ttta[:2]:
#                 if len(ttta)+1 >=len(line)>=len(ttta)-1:
#                     wrong_answers.append(line.strip())
#                 else:
#                     wrong_answers.append(line.strip())

#     return random.choices(wrong_answers,k =3)
   
#     # return random.choices(wrong_answers,k =3)

# # asn = {'w_ans':'',}
# asn = []
# asn = wrong_answers(ttta,d_lang)
# # w_answer = wrong_answers(ttta,d_lang)
# # print(asn)             
            


#     # for i in range(3):
#     #     wrong_answers.append(r_word.get_random_word())
#     # return wrong_answers



# selections_deployed= [ f'{asn[2]}',f'{asn[1]}',f'{asn[0]}', f'{ttta}++']
# np.random.shuffle(selections_deployed)
# print(selections_deployed)





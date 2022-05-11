from googletrans import Translator
import requests
from bs4 import BeautifulSoup as bs
from google.cloud import texttospeech
import re
import pandas
import numpy as np
import inflect
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/emreb/Documents/projects/secret/projecttelebotapi-cafc88105725.json'

# def dicti_brackets():


# data = {'number': '', 'word': ''}

# def dictionary(word):

#   url_merriam = 'https://www.merriam-webster.com/dictionary/'
#   page = requests.get(url_merriam+ word)
#   soup = bs(page.content, 'html.parser')
#   a = 3
#   m = soup.find_all('span', class_='dtText')[:3]
#   if m == []:

#       word = soup.find('p',class_='spelling-suggestion-text')
#       return [w.text for w in word]
#   else:

#     dictt= [c.text.split(':')[1].strip() for c in m]
#     return (','.join(str(a)for a in dictt)),a


# data['number'] = dictionary('apple')

# wrong_answer = ''
# number_answer = answers["number"][1]
# selections = ['ana', 'baba', f'{number_answer}']
# np.random.shuffle(selections)
# selections 
# print(data['number'][1])
# import glob
# All files and directories ending with .txt and that don't begin with a dot:
# dictt = []

# glob.glob("audio\*.mp3")
# for file in glob.glob("audio\*.mp3"):
#     dictt.append(file.split('\\')[1].split('.')[0])

# def wrong_answers():
#     glob.glob("audio\*.mp3")
#     return [file.split('\\')[1].split('.')[0] for file in glob.glob("audio\*.mp3")]

# dictt = wrong_answers()
# np.random.shuffle(dictt)
# correct_answer = 'apple'

# selections = [dictt[0], dictt[1], dictt[2], correct_answer]
# print(selections.index(f'{correct_answer}'))


# def translatetext(text,*args):
#     translator = Translator()
#     if args != ():
#         if len(args) == 1:
#             result = translator.translate(text, dest=args[0])
#         if len(args) == 2:
#             result = translator.translate(text, src=args[1], dest=args[0])
#     else:
#         result = translator.translate(text)

#     return result.text
# def number_level(number):
#     if number == '1':
#         k = np.random.randint(1,100)
#     if number == '2':
#         k = np.random.randint(100,1000)
#     if number == '3':
#         k = np.random.randint(1000,10000)
#     elif number != re.match('/[1-3]/',number):
#         k = 'You need to give 1,2,3 as level nothing else'
#     return k

# number = '5'
# print(re.match('[1-3]'
# 
# ,number) is None)
# with open('C:/Users/emreb/Documents/projects/secret/token.txt', 'r') as f:
#     token = f.read()

# print(token)
# print(number)
# k = number_level('1')
# print(k)
# correct_answer_index = dictt[f'{correct_answer}']


# print(dictt[1])

# expected_output=re.sub("]|[","",str(dcit))
# result = re.match(r'\["[^"]*"]', dcit)
# print(dcit)
# def translatetext(text,*args):
#     translator = Translator()
#     if args != ():
#         if len(args) == 1:
#             result = translator.translate(text, dest=args[0])
#         if len(args) == 2:
#             result = translator.translate(text, src=args[1], dest=args[0])
#         return result.text
#     else:
#         result = translator.translate(text)
#         return result.text

# # k = translatetext('que tal tolang tr',)
# # textt = 'que tal tolang tr moi aussi'

# # distint = textt.split('tolangg ')
# # try:
# #     destlang = distint[1]
# #     maintext = distint[0]   
# # except:
# #     spilit = textt.split()
# #     dest = spilit[-1]
# #     textlack = " ".join(spilit[:-1])
# # if len(distint) == 2:   
# #     print(destlang)
# # else:
# #     print(dest), print(textlack)
# def create_audio_number(src='en',dest='de'):

#   number = np.random.randint(1,100)
#   translator = Translator()
#   p = inflect.engine()
#   number_w = p.number_to_words(number)
#   result = translator.translate(number_w, src=src, dest=dest)
#   # Instantiates a client
#   client = texttospeech.TextToSpeechClient()
 
#   # Set the text input to be synthesized
#   synthesis_input = texttospeech.SynthesisInput(text=result.text)
  
#   # Build the voice request, select the language code ("en-US") and the ssml
#   # voice gender ("neutral")
#   voice = texttospeech.VoiceSelectionParams(
#     language_code= dest,
#     ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,)

#   # Select the type of audio file you want returned
#   audio_config = texttospeech.AudioConfig(
#     audio_encoding=texttospeech.AudioEncoding.MP3)

#   # Perform the text-to-speech request on the text input with the selected
#   # voice parameters and audio file type
#   response = client.synthesize_speech(
#         request={"input": synthesis_input, "voice": voice, "audio_config": audio_config}
#     )

#   # The response's audio_content is binary.
#   with open(f'audio/{result.text}.mp3', 'wb') as out:
#     # Write the response to the output file.
#     out.write(response.audio_content)
    
    
    
#   return result.text, open(f'audio/{result.text}.mp3', 'rb')

# create_audio_number()
def number_level(number):
  # k = 'asdaas'
  if number == '1':

    k = np.random.randint(1,100)
  if number == '2':
    k = np.random.randint(100,1000)
  if number == '3':
    k = np.random.randint(1000,10000)
  if re.match('[1-3]',number) is None:

    k = 'You need to give 1,2,3 as level nothing else'
  return k

# def create_audio_number(number,dest='de',src='en'):
#     number  = number_level(number)
#     # number = np.random.randint(10,1000)
#     translator = Translator()
#     p = inflect.engine()
#     number_w = p.number_to_words(number)
#     result = translator.translate(number_w, src=src, dest=dest)
#     #   Instantiates a client
#     client = texttospeech.TextToSpeechClient()
    
#     # Set the text input to be synthesized
#     synthesis_input = texttospeech.SynthesisInput(text=result.text)
    
#     # Build the voice request, select the language code ("en-US") and the ssml
#     # voice gender ("neutral")
#     voice = texttospeech.VoiceSelectionParams(
#         language_code= dest,
#         ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,)

#     # Select the type of audio file you want returned
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3)

#     # Perform the text-to-speech request on the text input with the selected
#     # voice parameters and audio file type
#     response = client.synthesize_speech(
#             request={"input": synthesis_input, "voice": voice, "audio_config": audio_config}
#         )

#     # The response's audio_content is binary.
#     with open('audio/question1.mp3', 'wb') as out:
#         # Write the response to the output file.
#         out.write(response.audio_content)
        
        
        
    # return result.text

number = number_level('2')
# number = np.random.randint(10,1000)
translator = Translator()
p = inflect.engine()
# number_w = p.number_to_words(number)
print(number)

# number = 2
# print(re.match('[1-3]',str(number)) is None)
# result = translator.translate(number_w, src=src, dest=dest)
# k = create_audio_number(2)
# print(k)
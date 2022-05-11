import os


from google.cloud import texttospeech
import requests
from bs4 import BeautifulSoup as bs
from google.cloud import texttospeech
import re
from random_word import RandomWords

import inflect
import pandas

from googletrans import Translator
import requests
from bs4 import BeautifulSoup as bs
from google.cloud import texttospeech
import re
from random_word import RandomWords

import inflect
import pandas
import numpy as np
import glob
import logging



os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/emreb/Documents/projects/secret/projecttelebotapi-cafc88105725.json'

def number_level(number):

    if number == '1':
        k = np.random.randint(1,100)
    if number == '2':
        k = np.random.randint(100,1000)
    if number == '3':
        k = np.random.randint(1000,10000)
    if re.match('[1-3]',str(number)) is None:

        k = 'You need to give 1,2,3 as level nothing else'
    
    return k


    
def create_audio_number(number,dest='de',src='en'):
    number  = number_level(str(number))
    # number = np.random.randint(10,1000)
    translator = Translator()
    p = inflect.engine()
    number_w = p.number_to_words(number)
    result = translator.translate(number_w, src=src, dest=dest)
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    
    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=result.text)
    
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code= dest,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,)

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
            request={"input": synthesis_input, "voice": voice, "audio_config": audio_config}
        )

    # The response's audio_content is binary.
    with open(f'audio/{result.text}.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        
        
        
    return  result.text
answers = {'number':'', 'words':''}
def answer_with_voice(textt):

    global answers
    textt = textt.split(' ')


    # return len (textt[0]) == 2
    if len(textt)==2:

        if len (textt[0]) == 2:
            hardness = textt[1]
            dest = (textt[0]).lower()
            return create_audio_number(hardness,dest)
    #         answers['number'] = create_audio_number(hardness,dest=dest)
    #         # return hardness,dest
    # else:
    #         answers['number'] = create_audio_number()

    # return hardness ,dest
# print(answer_with_voice('en 1'))
# print(answers)
# print()
# print(answers)
# number = '3'
# number  = number_level(number)
# translator = Translator()
# p = inflect.engine()
# number_w = p.number_to_words(number)
# # print(number_w)
# result = translator.translate(number_w,dest = 'de')
# print(result.text)
# # number = np.random.randint(10,1000)
print(create_audio_number(3,'de'))
# # number  = number_level(number)
# print(result.text)
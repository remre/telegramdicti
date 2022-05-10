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


def translatetext(text,*args):
    translator = Translator()
    if args != ():
        if len(args) == 1:
            result = translator.translate(text, dest=args[0])
        if len(args) == 2:
            result = translator.translate(text, src=args[1], dest=args[0])
        return result.text
    else:
        result = translator.translate(text)
        return result.text

# k = translatetext('que tal tolang tr',)
# textt = 'que tal tolang tr moi aussi'

# distint = textt.split('tolangg ')
# try:
#     destlang = distint[1]
#     maintext = distint[0]   
# except:
#     spilit = textt.split()
#     dest = spilit[-1]
#     textlack = " ".join(spilit[:-1])
# if len(distint) == 2:   
#     print(destlang)
# else:
#     print(dest), print(textlack)
def create_audio_number(src='en',dest='de'):

  number = np.random.randint(1,100)
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
    
    
    
  return result.text, open(f'audio/{result.text}.mp3', 'rb')

create_audio_number()
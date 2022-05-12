from google.cloud import texttospeech
from googletrans import Translator
import glob
import numpy as np
import re
from random_word import RandomWords
import os
import inflect
import requests
from bs4 import BeautifulSoup as bs
# from .transanddicttry import number_level
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/emreb/Documents/projects/secret/projecttelebotapi-cafc88105725.json'

class TransGoogle:



    def __init__(self,dest='de',number=None,src='en'):
        # self.random_word = random_word
        # if type(number) == int:
        self.number = number
        # self.args = args
        self.dest = dest
        self.src = src
        # self.g_number= g_number
        # self.translator = Translator()
        self.number2word = self.generate_random_number()
        self.word_gen = self.generate_random_word()
        # self.number_cas = selfnumber_level()
        # self.level_number = self.number_level(str(self.number))
        # if type(word) == str:
        #     self.word = word
        
   
    def generate_random_word(self):
        r_word = RandomWords()
        return r_word.get_random_word()

    
        
    def generate_random_number(self):
        
        # level_number = self.number_cas #number_level(str(self.number))
        level_number = number_level(str(self.number))
        p = inflect.engine()
        return p.number_to_words(level_number)
   
    
    def create_audio_file(self):
        translator = Translator()
        if self.number is None:
            text = translator.translate(self.word_gen, dest=self.dest, src=self.src).text
        else:
            text = translator.translate(self.number2word, dest=self.dest, src=self.src).text
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code=self.dest,
            ssml_gender = texttospeech.SsmlVoiceGender.NEUTRAL,)
        audio_config = texttospeech.AudioConfig(
            audio_encoding = texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(
            request={"input": synthesis_input, "voice": voice, "audio_config": audio_config}
        )
        with open('C:/Users/emreb/Documents/projects/telegramdicti/audio/QuizQuestion.mp3', 'wb') as out:
        # Write the response to the output file.
            out.write(response.audio_content)
        return open('C:/Users/emreb/Documents/projects/telegramdicti/audio/QuizQuestion.mp3', 'rb'), text

    


    def dest_and_level_seperator(self):
        pass


    def __str__(self):
        return f'{self.number}'

#  def translate_word(self):
#         translator = Translator()
#         if args != ():
#             if len(args) == 1:
#                 text = translator.translate(text, dest=args[0]).text
#                 if self.number:
#                     text = translator.translate(self.number2word, dest=self.dest, src=self.src).text
#                 if self.word:
#                     text = translator.translate(self.word_gen, dest=self.dest, src=self.src).text
#             if len(args) == 2:
#                 text = translator.translate(text, dest=args[0], src=args[1]).text
#         else:
#             if self.number:
#                     text = translator.translate(self.number2word, dest=self.dest, src=self.src).text
#             if self.word:
#                 text = translator.translate(self.word_gen, dest=self.dest, src=self.src).text
#             else:
#                 text = translator.translate(text).text
#         return text

def number_level(number):
            if number == '1':
                k = np.random.randint(1,100)
            if number == '2':
                k = np.random.randint(100,1000)
            if number == '3':
                k = np.random.randint(1000,10000)
            if re.match('[1-3]',(number)) is None:
                k = 'You need to give 1,2,3 as level nothing else'
            return k
def dictionary(word):

    url_merriam = 'https://www.merriam-webster.com/dictionary/'
    page = requests.get(url_merriam+ word)
    soup = bs(page.content, 'html.parser')
    m = soup.find_all('span', class_='dtText')[:3]

    if m == []:
        words = soup.find('p',class_='spelling-suggestion-text')
        dictt =  [w.text for w in words]
    else:
        dictt= [c.text.split(':')[1].strip() for c in m]

    return (','.join(str(a)for a in dictt))
def wrong_answers_number():
    glob.glob("audio\*.mp3")
    return [file.split('\\')[1].split('.')[0] for file in glob.glob("audio\*.mp3")]
  

# print(new_voice)


# new_word = TransGoogle('es')
# filee = new_word.create_audio_file()
# print(new_word)

# number = None
# number = str(number)
# print(number is None)

# def wrong_answers_number():
#     glob.glob("audio\*.mp3")
#     return [file.split('\\')[1].split('.')[0] for file in glob.glob("audio\*.mp3")]

# dictt_answers = wrong_answers_number()
# np.random.shuffle(dictt_answers)

# def create_audio_word(dest='de',src='en'):

#   translator = Translator()
#   r = RandomWords()
#   word = r.get_random_word()
#   result = translator.translate(word, src=src, dest=dest)
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
#   with open('audio/question_word.mp3', 'wb') as out:
#     # Write the response to the output file.
#     out.write(response.audio_content)
    
    
    
#   return result.text


# print(create_audio_word())

class Translatet:
    def __init__(self,text, *args):
        self.text = text
        self.args = args

    def translatetext(self):
        translator = Translator()
        if self.args != ():
            if len(self.args) == 1:
                result = translator.translate(self.text, dest=self.args[0])
            if len(self.args) == 2:
                result = translator.translate(self.text, src=self.args[1], dest=self.args[0])
        else:
            result = translator.translate(self.text)

        return result.text
    def __str__(self):
        return f'{self.text}'


# trial = Translatet('wilkommen','tr')
# print(trial.translatetext())
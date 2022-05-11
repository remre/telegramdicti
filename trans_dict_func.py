from google.cloud import texttospeech
from googletrans import Translator



class TransGoogle:



    def __init__(self,random_word,number,dest,src):
        self.random_word = random_word
        self.number = number
        self.dest = dest
        self.src = src
        self.translator = Translator()
        

    def create_random_word(self):
        pass
    def create_random_number(self):
        pass
    def translate_word(self):
        pass
    def create_audio(self):
        pass


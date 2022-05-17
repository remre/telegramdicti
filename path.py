import inflect
from bs4 import BeautifulSoup as bs
from googletrans import Translator



translator = Translator()
p = inflect.engine()
number = (34534,345345,347,312,124534211,24432)
text  = []
for i in number:
    # print(p.number_to_words(i))
    result = p.number_to_words(i)
    text = translator.translate(result, dest='es', ).text
    print(text)
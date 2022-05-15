import requests
from bs4 import BeautifulSoup as bs
def dictionary(word):

    url_merriam = 'https://www.merriam-webster.com/dictionary/'
    page = requests.get(url_merriam+ word)
    soup = bs(page.content, 'html.parser')
    m = soup.find_all('span', class_='dtText')[:3]

    if m == []:

        words = soup.find_all('p',class_='spelling-suggestions')[:2]
        dictt =  [w.text for w in words]
        dictt.append("Try again, The word you've entered isn't in the dictionary maybe some suggestions shown above.")
    else:
        try:
            dictt= [c.text.split(':')[1].strip() for c in m]
        except:
            dictt = [c.text.strip() for c in m]

    return (','.join(str(a)for a in dictt))

wordi = dictionary('go away')

print(wordi)
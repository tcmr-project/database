import requests
from bs4 import BeautifulSoup

# xml형식으로 저장하기
f = open('./data/text.xml', 'w')

#api키 넣기
raw = requests.get('apikey')
html = BeautifulSoup(raw.text, 'html.parser')

f.write(html)

f.close()
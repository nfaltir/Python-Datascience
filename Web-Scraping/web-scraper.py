import requests
from bs4 import BeautifulSoup
import pandas as pd 



url = 'https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_(A)'
response = requests.get(url)

print(response)



#print html content
#print(response.content)

#beautify by using beautiful soup using 'prettify'

soup = BeautifulSoup(response.text, 'lxml')
#print(soup.prettify)


data = soup.find_all('a', class_='external text')
for symb in data:
  print(symb.text)

 

url = 'https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_(B)'
response = requests.get(url)

print(response)

soup = BeautifulSoup(response.text, 'lxml')
#print(soup.prettify)


data = soup.find_all('a', class_='external text')
for symb in data:
  print(symb.text)


print("\ntotal list\n",symb.text)
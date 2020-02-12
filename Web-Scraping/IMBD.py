from bs4 import BeautifulSoup
import requests
import lxml
import string
import pandas as pd
import csv


url = 'https://www.imdb.com/search/title/?count=100&groups=oscar_best_picture_winners&sort=year%2Cdesc&ref_=nv_ch_osc'


response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#data = soup.findAll('div',class_='consumer-information__name')
movie_title = soup.find('div', class_='lister-item-content')


for titles in movie_title:
  print(titles.text)
  
  

  

  
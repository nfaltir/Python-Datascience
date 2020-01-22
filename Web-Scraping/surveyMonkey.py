from bs4 import BeautifulSoup
import requests
import lxml
import string
import pandas as pd

url = 'https://www.trustpilot.com/review/surveymonkey.com'

response = requests.get(url)
print("web response:", response)

soup = BeautifulSoup(response.text, 'lxml')
#data = soup.findAll('div',class_='consumer-information__name')
data1=soup.findAll('p', class_='review-content__text') 

for stars in data1:
  print(stars.text)




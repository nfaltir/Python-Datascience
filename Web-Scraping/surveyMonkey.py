from bs4 import BeautifulSoup
import requests
import lxml
import string
import pandas as pd


#A dictionary of webpages to scrap
url = ["https://www.trustpilot.com/review/surveymonkey.com",
"https://www.trustpilot.com/review/surveymonkey.com?page=1",
"https://www.trustpilot.com/review/surveymonkey.com?page=2",
"https://www.trustpilot.com/review/surveymonkey.com?page=3",
"https://www.trustpilot.com/review/surveymonkey.com?page=4",
"https://www.trustpilot.com/review/surveymonkey.com?page=5",
"https://www.trustpilot.com/review/surveymonkey.com?page=6"]

for pages in url:
  response = requests.get(pages)
  soup = BeautifulSoup(response.text, 'lxml')
  #data = soup.findAll('div',class_='consumer-information__name')
  data1=soup.findAll('p', class_='review-content__text') 

  for review_comments in data1:
    print(review_comments.text)



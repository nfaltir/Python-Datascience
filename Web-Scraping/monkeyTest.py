from bs4 import BeautifulSoup
import requests
import lxml
import string
import pandas as pd

url = ["https://www.trustpilot.com/review/surveymonkey.com",
"https://www.trustpilot.com/review/surveymonkey.com?page=1",
"https://www.trustpilot.com/review/surveymonkey.com?page=2",
"https://www.trustpilot.com/review/surveymonkey.com?page=3",
"https://www.trustpilot.com/review/surveymonkey.com?page=4",
"https://www.trustpilot.com/review/surveymonkey.com?page=5",
"https://www.trustpilot.com/review/surveymonkey.com?page=6"]

for pages in url:
  print(pages)



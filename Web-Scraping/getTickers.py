from bs4 import BeautifulSoup
import requests
import lxml
import string
import pandas as pd
import yfinance as yf

#get all stock tickers
def tickers():

  url = 'https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_'
  abc = ['(a)','(b)','(c)','(d)','(e)','(f)','(g)','(h)','(i)','(j)','(k)','(l)','(m)','(n)','(o)','(p)','(q)','(r)','(s)','(t)','(u)','(v)','(w)','(x)','(y)','(z)']
  #timeFrame = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

  for i in abc:
    sList = (str.upper(i))
    all_url = url+sList
    response = requests.get(all_url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('a', class_='external text')
    for symb in data:
      allTickers = symb.text
      print(allTickers)

print(tickers())

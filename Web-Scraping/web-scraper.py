import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_(A)'

response = requests.get(url)
print(response)

#print html content
#print(response.content)

#beautify by using beautiful soup using 'prettify'

soup = BeautifulSoup(response.text, 'lxml')
#print(soup.prettify)

#find all coffee shop names in portland
data = soup.find_all('a')
data1 = soup.find_all('td',{'class':'ratingColumn imdbRating'})

reviewCount = soup.find_all('td',{'class':'ratingColumn'})
for reviews in reviewCount:
    print(reviews.getText())
    
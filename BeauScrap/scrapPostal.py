# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

page = urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')
# get the index price
price_box = soup.find('div', attrs={'class':'price'})
print(price_box)
price = price_box.text
print(price)
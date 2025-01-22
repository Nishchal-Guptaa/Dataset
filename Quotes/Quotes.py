import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

quotes_list = []
author_list = []
for page_num in range(1,11):
    url = f"https://quotes.toscrape.com/page/{page_num}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    quotes = soup.findAll('span', attrs={"class":"text"})
    authors = soup.find_all('small', attrs={'class':'author'})
    for quote in quotes:
        quotes_list.append(quote.text)
    for author in authors:
        author_list.append(author.text)

data = {
    'Quotes': quotes_list,
    'Authors': author_list
}

df = pd.DataFrame(data)

folder = 'Quotes'
file_name = "Some Famous Quotes by Some Famous Authors.csv"

file = os.path.join(folder,file_name)

df = pd.DataFrame(data)
df.to_csv(file)
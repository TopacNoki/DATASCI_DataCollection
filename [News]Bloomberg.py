# -*- coding: utf-8 -*-
"""[DATASCI] DataCollection_NYTimes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gySliNvXmpLNI1S3Dfp4dwSPm80SG3ER
"""

!pip install newsapi-python

import json
from newsapi import NewsApiClient
from google.colab import files

apiKey = '5e613a6f87a64f5ea96769f005b5917d'
URL ='bloomberg.com'
pageSize = 80

newsapi = NewsApiClient(api_key=apiKey)
all_articles = newsapi.get_everything(domains = URL,from_param='2021-03-11', to='2021-03-12', language='en', page=1, page_size=pageSize)

newsArticles = all_articles['articles']

article_list = []
for article in newsArticles:
    article_list.append({
        'source': article['source'],
        'date': article['publishedAt'],
        'title': article['title'],
        'content': article['content'],
        'author': article['author']
    })

with open('article_list.json', 'w', encoding='utf-8') as f:
    json.dump(article_list, f, ensure_ascii=False, indent=4)

files.download('article_list.json')

article_list
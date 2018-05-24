from bs4 import BeautifulSoup
from urllib import request
import re
from time import time

DAUM_URL = "http://dic.daum.net"

def craete_soup_with_url(url):
    handler = request.urlopen(url)
    source = handler.read().decode('utf-8')
    return BeautifulSoup(source, 'html.parser')

def create_soup_with_query(query):
    url = DAUM_URL+'/search.do?dic=eng&q=' + query
    return craete_soup_with_url(url)

def create_soup_with_wordid(wordid):
    url = DAUM_URL+'/word/view.do?wordid=' + wordid
    return craete_soup_with_url(url)

def get_wordid(url):
    return re.findall('ekw[\d]+', url)[0]

def get_meaning(query):
    soup = create_soup_with_query(query)
    refresh_meta = soup.find('meta', attrs={'http-equiv': 'Refresh'})
    if refresh_meta is not None:
        wordid = get_wordid(refresh_meta.get('content'))
        soup = create_soup_with_wordid(wordid)
        meaning = soup.find('ul', class_='list_mean').get_text()
        return query, meaning

    final_page_anchor = soup.find('a', class_='txt_cleansch')
    if final_page_anchor is not None:
        wordid = get_wordid(final_page_anchor.get('href'))
        soup = create_soup_with_wordid(wordid)
        meaning = soup.find('ul', class_='list_mean').get_text()
        return query, meaning

import asyncio

async def get_meaning_all(word_list):
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(None, get_meaning,i) for i in word_list
    ]
    return await asyncio.gather(*futures)

t1 = time()
loop = asyncio.get_event_loop()
word_list = ["a", "the", "to", "where", "an", "which", "or", "how", 
    "can", "should", "would", "shall", "as", "like", "you", "for", "in", "of",
    "your", "I", "will", "from"]
l = loop.run_until_complete(get_meaning_all(word_list))
print (l)
t2 = time()
loop.close()
print (t2-t1)

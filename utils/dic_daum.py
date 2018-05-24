from bs4 import BeautifulSoup
from urllib import request
import re
import asyncio

DAUM_URL = "http://dic.daum.net"

def craete_soup_with_url(url):
    handler = request.urlopen(url, )
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
    if not is_ascii(query):
        return "", ""

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

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

async def get_meaning_all(word_list):
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(None, get_meaning,i)for i in word_list
    ]
    return await asyncio.gather(*futures)

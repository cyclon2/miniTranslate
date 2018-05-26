# -*- coding: cp949 -*-
from bs4 import BeautifulSoup
from urllib import request
import re
import asyncio

DAUM_URL = "http://dic.daum.net"
SUBURL = "http://alldic.daum.net/word/view_supword.do?"

def craete_soup_with_url(url):
    handler = request.urlopen(url)
    source = handler.read().decode(handler.headers.get_content_charset())
    return BeautifulSoup(source, 'html.parser')

def create_soup_with_query(query):
    url = DAUM_URL+'/search.do?dic=eng&q=' + query
    return craete_soup_with_url(url)

def create_soup_with_wordid(wordid):
    url = DAUM_URL+'/word/view.do?wordid=' + wordid
    return craete_soup_with_url(url)

def create_soup_with_wordid_and_subid(wordid, subid):
    url = SUBURL+ "wordid=%s&supid=%s&suptype=KUMSUNG_EK" %(wordid, subid)
    return craete_soup_with_url(url)

def get_wordid(url):
    return re.findall('ekw[\d]+', url)[0]
        
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

async def search_rough_all(word_list):
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(None, search, i)for i in word_list
    ]
    return await asyncio.gather(*futures)

async def search_detail_all(word_list):
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(None, search, i, False)for i in word_list
    ]
    return await asyncio.gather(*futures)

def create_soup_for_subid(soup, wordid):
    wordsubid = soup.find('div', class_='box_word').get('data-supid')
    soup = create_soup_with_wordid_and_subid(wordid, wordsubid)
    return soup

def get_meaning_rough(soup, wordid):
    soup = create_soup_with_wordid(wordid)
    meaning = soup.find('ul', class_='list_mean').get_text()
    print(meaning)
    return meaning

def get_meaning_detail(soup, wordid):
    soup = create_soup_with_wordid(wordid)
    soup = create_soup_for_subid(soup, wordid)
    meanings = soup.find_all('div', class_='fold_ex')
    meaning = []
    import itertools
    for m in meanings:
        text = re.sub(r'([\t|\n])+', '', m.get_text().replace('  ', ''))
        meaning.append(text)
    meaning = "\n".join(meaning)
    return meaning

def get_meaning(soup, wordid, is_rough):
    if is_rough:
        return get_meaning_rough(soup, wordid)
    else:
        return get_meaning_detail(soup, wordid)

def search(query, is_rough=True):
    if not is_ascii(query):
        return "", ""

    soup = create_soup_with_query(query)
    refresh_meta = soup.find('meta', attrs={'http-equiv': 'Refresh'})
    if refresh_meta is not None:
        wordid = get_wordid(refresh_meta.get('content'))
        return query, get_meaning(soup, wordid, is_rough)

    final_page_anchor = soup.find('a', class_='txt_cleansch')
    if final_page_anchor is not None:
        wordid = get_wordid(final_page_anchor.get('href'))
        return query, get_meaning(soup, wordid, is_rough)

if __name__ == "__main__":
    print(search("hello", False))
    # search("as", False)

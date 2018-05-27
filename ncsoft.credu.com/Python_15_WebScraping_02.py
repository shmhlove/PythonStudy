#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

import pyautomate
from pyautomate import web

def search_google(keyword):
    url = "http://google.com/search?q={0}".format(keyword);
    html = web.parse_htm(url);
    return html.select('.r a');

bitcoin = search_google('bitcoin');
print(bitcoin);

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

urls = web.get_urls(bitcoin);
for text, url in urls:
    print(text, url);

print(urls[0].url);

start = urls[0].url.find('http');
print(start);

url = urls[0].url[start:];
pirnt(url);

def extract_google_url(url):
    start = url.find('http');
    return url[start:];

print(extract_google_url(urls[0].url));

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

def search_naver(keyword, section):
    url = "https://search.naver.com/search.naver?query={0}".format(keyword);
    html = web.parse_html(url);
    selector = '{}.section a.link'.format(section);
    return html.select(selector);

result = search_name('bitcoin', section='webdoc');
print(result);

urls = web.get_urls(result);
for text, url in urls:
    print(text, url);

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

from pandas import DataFrame

table = DataFrame(urls);
print(table);

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

import webbrowser

print(webbrowser.open('http://kr.plaync.com'));

for text, url in urls:
    webbrowser.open(url);

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------


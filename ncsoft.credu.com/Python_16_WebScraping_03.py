#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

import pyautomate
from pyautomate import web

def search_google(keyword):
    url = "http://google.com/search?q={0}".format(keyword);
    html = web.parse_htm(url);
    return html.select('.r a');

def search_naver(keyword, section):
    url = "https://search.naver.com/search.naver?query={0}".format(keyword);
    html = web.parse_html(url);
    selector = '{}.section a.link'.format(section);
    return html.select(selector);

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

web.setup_webdriver(2.33);

chrome = web.get_brower('./chromedriver');
chrome.get('http://www.naver.com');
search_box = chrome.find_element_by_css_selector('#query');
search_box.send_keys('파이썬');
search_box.send_keys(web.Keys.RETURN);
chrome.quit();

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

chrome = web.get_brower('./chromedriver');
chrome.get('http://www.naver.com');
search_box = chrome.find_element_by_css_selector('#query');
search_box.send_keys('파이썬', web.Keys.RETURN);
search_results = chrome.find_element_by_css_selector('.webdoc.section a.link');
print(search_results[0].get_attribute('href'));
urls = web.get_urls(search_results);
for text, url in ruls:
    print(text, url);
chrome.quit();

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

from pandas import DataFrame
from pyautomate import office

frame = DataFrame(urls);
print(frame);

office.to_excel(frame, 'search_python.xlsx');

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

html = seb.parse_html('http://finance.naver.com');
html.select('.num_quot .num');

import time
chrome = web.get_brower('./chromedriver');
chrome.get('http://finance.naver.com');
print('페이지 로딩 ...');

kospi_index = [];
for i in range(10):
    element = chrome.find_element_by_css_selector('.num_quot .num');
    timestamp = chrome.find_element_by_css_selector('#time');

    kospi = element.text;
    print(timestamp.text, kospi);

    kospi_index.append((kospi, timestamp.text));

    time.sleep(10);

chrome.quit();

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

frame = DataFrame(kospi_index);
print(frame);

office.to_excel(frame, 'search_kospi.xlsx');

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------
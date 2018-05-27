#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

import pyautomate
from pyautomate import web
from pyautomate import office
from padars import DataFrame

web.setup_webdriver(2.33);

chrome = web.get_brower('./chromedriver');
chrome.get('http://news.jtbc.join.com');
html = web.html.Html(chrome.page_source);

elements = html.select('#jtbcBody a');
print(elements[:3]);

links = web.get_urls(elements);
print(links[:3]);

jtbc_articles = DataFrame(links);
print(jtbc_articles[:10]);

elements = html.select('#jtbcBody a[href^="http://news.jtbc.joins.com/html"]');
links = web.get_urls(elements);
frame = DataFrame(links);
frame[:10];

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

timestamp = pyautomate.get_timestamp();
office.to_excel(frame, 'jtbc_{}.xlsx'.format(timestamp));

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

def get_articles(html, selector):
    elements = html.select(selector);
    links = web.get_urls(elements);
    articles = DataFrame(links);
    return articles;

with open('data/news_websites.txt') as f:
    news_websites = [];
    for line in f:
        line = line.strip();
        if line:
            title, url, selector = line.split('|');
            news_websites.append((title, url, selector));

news_articles = [];
for title, url, selector in news_websites:
    chrome.get(url);
    html = web.html.Html(chrome.page_source);
    articles = get_articles(html, selector);
    articles.name = title;
    news_articles.append(articles);

timestamp = pyautomate.get_timestamp();
office.to_excel(news_articles, 'news_{}.xlsx'.format(timestamp));

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

import getpass

user = input('username: ');
password = getpass.getpass('password: ');

chrome.get('http://www.naver.com');
login_id_box = chrome.find_element_by_id('id');
login_id_box.send_keys(user);
login_pass_box = chrome.find_element_by_id('pw');
login_pass_box.send_keys(password);
login_btn = chrome.find_element_by_css_selector('.btn_login input');
login_btn.click();
chrome.quit();

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

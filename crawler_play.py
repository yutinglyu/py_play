import urllib
import bs4
import requests
import time

start_url = 'https://en.wikipedia.org/wiki/Special:Random'
target_url = 'https://en.wikipedia.org/wiki/Philosophy'

crawler_log = [start_url]

def crawl(search_history, target_url, max_crawls = 5):
    if search_history[-1] == target_url:
        print('We have found it. Yeah!!!!!!!!!')
        return False
    elif search_history[-1] in search_history[:-1]:
        print('It is a looop!!!!!!!!')
        return False
    elif len(search_history) > max_crawls:
        print('OMG, maybe we can\'t find it.')
        return False
    else:
        return True
    
def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    content_div = soup.find(id = 'mw-content-text').find(class_ = 'mw-parser-output')
    
    name_link = None
    for element in content_div.find_all('p', recursive = False):
        if element.find('a', recursive = False):
            name_link = element.find('a', recursive = False).get('href')
            break
        first_link = urllib.parse.urljoin('https://en.wikipedia.org', name_link)
        return first_link

while crawl(crawler_log, target_url):
    print(crawler_log[-1])
    
    first_link = find_first_link(crawler_log[-1])
    if not first_link:
        print('There is no first link here. I am going home.')
        break
    crawler_log.append(first_link)
    
    time.sleep(0.1)
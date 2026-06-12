'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to 
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.

'''

'''

https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/
'''

import threading
import requests
from bs4 import BeautifulSoup #for webscraping

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',

'https://docs.langchain.com/oss/python/langchain/install',

'https://python.langchain.com/v0.2/docs/tutorials/'

] #webpages to scrap from

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser') #(content,parser to use)
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread) #add threads in list and start
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")
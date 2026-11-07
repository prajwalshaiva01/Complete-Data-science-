import threading
import requests
from bs4 import BeautifulSoup

urls=[
'https://docs.langchain.com/oss/python/langchain/overview',
'https://docs.langchain.com/oss/python/langchain/messages',
'https://docs.langchain.com/oss/python/langchain/tools'
]
def fetch_content(url1):
    response=requests.get(url1)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)} characters from{url1}")


thread=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    thread.append(thread)
    thread.start()

for thread in thread:
    thread.join()

print("All web pages fetche")
import requests
from bs4 import BeautifulSoup

user_input = input("enter something to search :")
website= "https://www.bing.com/search?q="+ user_input

headers = {
        'User-Agent':
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
        }#Linux

request= requests.get(website, headers=headers)
webContent= BeautifulSoup(request.content, 'html.parser')

listContent= webContent.find_all('ol')

for content in listContent:
        liContent= content.find_all('li')
        for content in liContent:
                divContent= content.find('div')
                if divContent==None:
                        pass
                else:
                        h2Content= divContent.find('h2')
                        if h2Content==None:
                                pass
                        else:
                                aContent= h2Content.find('a').get('href')
                                if aContent==None:
                                     pass
                                else:
                                        print(aContent)
from tkinter import ANCHOR
from turtle import title
import requests
from bs4 import BeautifulSoup
url = "https://mangareader.to/"

r=requests.get(url)
htmlcontent=r.content

soup=BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify)

#TREE TRAVERSAl

title=soup.title
#print(title.string)
#anchor=soup.find("a")
#print(soup.find_all('div',class_='modal-body'))
#print(soup.find_all('div'))
#print(soup.find('a').get_text())
#print(soup.get_text())




anchor=soup.find_all('a')
all_links=set()
for links in anchor:
     if(links.get('href')!='#'):
        linktext="https://mangareader.to/" + links.get('href')
        all_links.add(links)
        print(linktext)




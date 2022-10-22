from logging import exception
from operator import le
from tkinter import W
import requests
import openpyxl
from bs4 import BeautifulSoup

'''TO OPEN A NEW EXCEL FILE'''
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="TOP 250 MOVIES ACCORDING TO IMDB RATING"
sheet.append(['RANK','MOVIE NAME','YEAR','RATING'])

try:
    source=requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status()
    soup=BeautifulSoup(source.text,'html.parser')
    movies= soup.find('tbody', class_='lister-list').find_all('tr')
    for movie in movies:
        name=movie.find('td', class_='titleColumn').a.text
        rank=movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        year=movie.find('td', class_='titleColumn').span.text.strip('()')
        rate=movie.find('td', class_='ratingColumn imdbRating').strong.text
        print(rank, name , year, rate)
        sheet.append([rank, name , year, rate])

except Exception as e:
    print(e)

excel.save('IMDB MOVIE RATING.xlsx')
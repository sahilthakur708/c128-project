from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
from selenium.webdriver.common.by import By
import pandas as pd

start_url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser=webdriver.Chrome('C:/Users/admin/OneDrive/Desktop/c128 project/chromedriver.exe')
browser.get(start_url)

time.sleep(10)

headers=['star','distance','brown_dwarf','mass','radius']
stars_data=[]

star=[]
distance=[]
brown_dwarf=[]
Radius=[]
mass=[]

def scrape ():
    soup=BeautifulSoup(browser.page_source,'html.parser')
    star_table=soup.find_all('table')

    star.append(star_table[1].text)
    distance.append(star_table[6].text)
    brown_dwarf.append(star_table[8].text)
    Radius.append(star_table[10].text)
    mass.append(star_table[9].text)
    
  
scrape()

df2 = pd.DataFrame(list(zip(star,distance,mass,Radius,brown_dwarf)),columns=['Star_name','Distance','Mass','Radius','Brown_dwarf'])
print(df2) 
df2.to_csv('bright_stars.csv')



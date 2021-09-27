# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:59:05 2019

@author: sahi hai
"""

#pip install PyPDF2

"""

from PyPDF2 import PdfFileReader

PDFfilename = "C:\\Users\\sahi hai\\Desktop\\TCS\\TCS offer letter.pdf" #filename of your PDF/directory where your PDF is stored
f = open(PDFfilename, 'rb')

pfr = PdfFileReader(f) #PdfFileReader object

print(pfr.numPages)


page_one = pfr.getPage(1)
page_one_text = page_one.extractText()
print(page_one_text)

f.close()

"""

import requests
import bs4

result = requests.get('http://quotes.toscrape.com/')
#print(result.text)

soup=bs4.BeautifulSoup(result.text,'lxml')
#print(soup.select('.author'))

"""
# For printing Author names
author_set = set()

for auth in (soup.select('.author')):
    author_set.add(auth.text)

print( author_set)

# for getting top 10 tags
tags = soup.select('.tag-item')
tag_list = []

for tag in tags:
    tag_list.append(tag.text)
print(tag_list)

"""

"""
quotes = soup.select('.text')
print(quotes[0].text)

quote_list=[]
for quote in quotes:
    quote_list.append(tag.text)
print(quote_list)
"""

url ='https://quotes.toscrape.com/page/'

page_url = url + str(999999999)
res = requests.get(page_url)
soup = bs4.BeautifulSoup(res.text,'lxml')



page_still_valid = True
authors = set()

page = 1

while page_still_valid:
    page_url = url +str(page)
    
    res = requests.get(page_url)
    
    if "No quotes found" in res.text:
        break
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    for name in soup.select(".author"):
        authors.add(name.text)
    
    
    page = page + 1
    


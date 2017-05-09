#!/usr/env python 
from bs4 import *
import requests

#use the request package to make the request
menu = requests.get("http://www.usask.ca/culinaryservices/agriculture-menu.php")

#check that the request worked
#print(menu.text)

#use beautiful soup to parse the HTML available from the request object (menu) 
lunch = BeautifulSoup(menu.text, 'html.parser')

print
#print(lunch.get_text())
for i in lunch.find_all('p'): 
  if "University" not in i.text:
    print(i.text)

#text = lunch.prettify().split('\n')
#linenum = 0
#for i in text: 
# linenum = linenum + 1
# print str(text[linenum]) 


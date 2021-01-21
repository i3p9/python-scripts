import requests
from bs4 import BeautifulSoup
import re

con = input("Which country: ")
URL = 'https://www.worldometers.info/coronavirus/country/'+con
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='content-inner')
cases =results.find_all('div', class_=('maincounter-number'))

numbers = []

for cases in cases:
    total_case = cases.find('span')
    total_case_num = total_case.text
    numbers.append(total_case_num)

#with open("out.txt", "a") as f:
#    print("This is a test", file=f)
    
print("For",con,">total cases:", numbers[0], "deaths:", numbers[1], "recovered:", numbers[2])
import requests
from bs4 import BeautifulSoup
import time
import csv

from datetime import date

url = "https://www.tripadvisor.com/Restaurant_Review-g303876-d1809988-Reviews-Sweet_Magic-Vijayawada_Krishna_District_Andhra_Pradesh.html"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

html_page = requests.get(url, headers=headers)
soup = BeautifulSoup(html_page.content, 'lxml')

edo = soup.find("div" , class_="pageNumbers")
links = edo.find_all(href=True)
links_next = []



for link in links:
    links_next.append("https://www.tripadvisor.com" + link['href'])

# for link_next in links_next:
#     print(link_next)



csv_file=open("reviews.csv","w", newline="",encoding='utf-8')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['review','decide'])



for link_nextt in links_next:
    url = link_nextt
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    html_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_page.content, 'lxml')
    data = soup.find_all("span" , class_="noQuotes")
    for x in data:
        v = x.get_text()
        #print(v)
        csv_writer.writerow([v])
        
    time.sleep(3)


csv_file.close()











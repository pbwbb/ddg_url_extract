from tkinter import Tk     
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup
import urllib.parse

file_path = askopenfilename()
with open(file_path, 'r',encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser').find_all("a", href=True)
for link in soup:
    url = link['href'].split('=')[1].strip()
    url = url.split('&rut')[0].strip()
    decoded_url = urllib.parse.unquote(link)
    with open('extracted_urls.txt', 'a',encoding='utf-8') as file:
        file.write(decoded_url + '\n')
    

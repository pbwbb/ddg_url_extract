from tkinter import Tk     
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup
import urllib.parse
print("Duckduckgo html URL extractor by Pedro Webber -> https://github.com/pbwbb/ddg_url_extract")
file_path = askopenfilename()
with open(file_path, 'r',encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser').find_all("a", href=True)
for link in soup:
    try:
        if "duckduckgo.com" in link:
            url = link['href'].split('uddg=')[1]
            print(url)
            url = url.split('&rut')[0].strip()
            decoded_url = urllib.parse.unquote(url)
            print(decoded_url)
            with open('extracted_urls.txt', 'a',encoding='utf-8') as file:
                file.write(decoded_url + '\n')
        else:
            url = link['href']
            decoded_url = urllib.parse.unquote(url)
            print(decoded_url)
            with open('extracted_urls.txt', 'a',encoding='utf-8') as file:
                file.write(decoded_url + '\n')
    except:
        pass
        

    

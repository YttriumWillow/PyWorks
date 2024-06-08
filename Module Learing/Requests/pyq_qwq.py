import requests as req
from bs4 import BeautifulSoup
import demjson as dj

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
url = "https://api.shadiao.app/pyq"
pyqfile = req.get(url, headers = header)
# soup = BeautifulSoup(pyqfile.text, "lxml")
# names = soup.select("body > pre")
# print(pyqfile.text)

text = dj.decode(pyqfile.text)
print(text["data"]["text"])



"""
with open("img.png", "wb") as f:
    f.write(imgfile.content)
"""

#app > div.main-container > main > div > div > div > div.border.table > div.row-wrap > div:nth-child(1) > span.pid
#app > div.main-container > main > div > div > div > div.border.table > div.row-wrap > div:nth-child(1) > div.title > a
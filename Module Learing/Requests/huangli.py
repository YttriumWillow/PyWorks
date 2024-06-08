import requests
from bs4 import BeautifulSoup
import time
'''
///////
'''
class Tb():
    def __init__(self):
        self.URL = "http://www.atoolbox.net/Tool.php?Id=922"
        self.header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    def get_tb(self):
        tb_html = requests.get(self.URL, headers = self.header)
        soup = BeautifulSoup(tb_html.text, "lxml")
        # names = soup.select("#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)")
        print(soup)

tb = Tb()
tb.get_tb()
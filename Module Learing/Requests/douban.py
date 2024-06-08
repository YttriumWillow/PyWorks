import requests
from bs4 import BeautifulSoup
import time
'''
https://www.163.com/robots.txt
https://movie.douban.com/robots.txt
'''
'''
https://movie.douban.com/top250
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
document.querySelector("#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)")
'''
class Douban():
    def __init__(self):
        self.URL = "https://movie.douban.com/top250"
        self.header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    def get_douban250(self):
        for i in range(0, 226, 25):# headers = self.header, 
            douban_html = requests.get(self.URL, headers = self.header, params = {'start' : str(i)})
            soup = BeautifulSoup(douban_html.text, "lxml")
            names = soup.select("#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)")
            print(names)
            time.sleep(0.1)

douban = Douban()
douban.get_douban250()
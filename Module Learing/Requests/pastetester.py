import requests
from bs4 import BeautifulSoup
import time
pastes = [
"qheqtoex",
"frryjaev",
"rdbmkxik",
"ckecjnuw",
"lqtvtfdw",
"zzrqvcdm",
"bkqosyvd",
"umdklrft",
"cxkmpcjk",
"vulgflpl",
"nuitmubq",
"ysvlajoe",
"zgaiiuwo",
"xxpgxmty",
"pqbsldem",
"waudsvft",
"wzklxqnt",
"hntwfigd",
"dasxnjya",
"toxpxfoy",
"anqavbht",
"bwdprrbv",
"vzfdtsqg",
"yvkovlza",
"npkhxwgq",
"wzgheoum",
"ilxhiosq",
"vfuywxej",
"aeqrmzsr",
"tqjbeunp",
"iqyaijgt",
"cunqsjng",
"onvqtrub",
"zhxenyhw",
"pemxaudj",
"zgietjtl",
"onlhektg",
"caetgvkb",
"xodyxalo",
"zuouyqzo",
"fkiviapx",
"eqfqtrxv",
"jypdokax",
"uxskvfvu",
"eigvvoll",
"dardwpsj",
"jtjvciox",
"nqflzprk",
"pnowviir",
"lxtupqvy",
"efxwrpuh",
"kegjqdas",
"hntpjlee",
"denlgywp",
"qkczfcdz",
"qqccnkzq",
"ixkgdoev",
"abxmuprv",
"vjdtdjvq",
"mpbejeci",
"dravkjmp",
"atqahdhb",
"jcwnzkln",
"fgyooxsp",

]

URL = "https://www.luogu.com.cn/paste/"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.86"}

for i in pastes:
    faq_html = requests.get(URL + i, headers = header)
    soup = BeautifulSoup(faq_html.text, "lxml")
    txt = str(soup)
    # print(txt)
    if "未找到" in txt:
        print("failed:", i)
    if "Level" in txt:
        print("!!!!!!!!!", i)
    time.sleep(0.1)


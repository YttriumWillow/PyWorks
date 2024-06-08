import requests
import re

def get_html(url):
    return requests.get(url,headers=headers1).text

def parse(html):
    video_name=re.findall('<span class="tit">(.*?)</span>',html,re.S)[0]+'.flv'#本来是m4s，但是电脑打不开所以还是用flv
    print("正在爬取"+video_name+"...")
    video_url=re.findall('window.__playinfo__={.*?"baseUrl":"(.*?)".*?}',html,re.S)[0]
    # print(video_url)
    return video_url,video_name

def download(videourl,video_name):
    with open(video_name,'wb') as f:
        f.write(requests.get(videourl,headers=headers2,stream=True,verify=False).content)
    f.close()
    print("视频下载完成!")


if __name__ == '__main__':
    avid=input("请输入要爬取的视频url:")
    base_url=avid
    headers1={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Host': 'www.bilibili.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive'
    }

    headers2={
        'Host':'cn-jsnj3-cmcc-v-14.bilivideo.com',
        'Accept-Encoding':'identity',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Origin':'https://www.bilibili.com',
        'Referer':base_url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    html=get_html(base_url)
    videourl,videoname=parse(html)
    download(videourl,videoname)
    

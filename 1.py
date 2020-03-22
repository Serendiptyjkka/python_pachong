import requests

params = {
    'wd': '中国'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
}
response = requests.get("http://www.baidu.com/s", params=params,  headers=headers)
with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))
print(response.url)
import requests
from lxml import etree

headers = {
    'User-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400",
    'Referer': 'https://www.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/ganzhou/'
response = requests.get(url, headers=headers)
text = response.text

html = etree.HTML(text)
ul = html.xpath("//ul[@class= 'lists']")[0]
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0]

    movie = {
        'title': title,
        'region': region,
        'director': director,
        'actors': actors,
        'thumbnall': thumbnail,
    }

    movies.append(movie)

print(movies)







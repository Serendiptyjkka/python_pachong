from lxml import etree
import requests

BASE_DOMAIN = 'https://www.dytt8.net/'
HEADERS = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
}


def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url: BASE_DOMAIN+url, detail_urls)
    return detail_urls


def parse_detail_page(url):
    movies = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode("gbk")
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']")[0]
    movies['title'] = title


def spider():
    base_url = 'https://www.dytt8.net//html/gndy/dyzz/list_23_{}.html'
    for x in range(1, 8):
        print("*"*30)
        print(x)
        print("*"*30)
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
           movie =  parse_detail_page(detail_url)
        print(movie)
        break


if __name__ == '__main__':
    spider()


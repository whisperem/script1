import requests
from bs4 import BeautifulSoup
import json

def get_page():
    # 1.url
    url = "https://movie.douban.com/cinema/nowplaying/jinzhong/"
    # 2.请求页面时候应该发送什么数据
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    # 3.请求方法GET
    # 4.发送请求
    response = requests.get(url, headers=headers)
    text = response.text
    return text #返回text值进行解析
    # print(response.text)

# 解析：提取所需信息
def parse_page(text):
    soup = BeautifulSoup(text,'lxml')
    movies = []
    liList = soup.find_all("li",attrs={"data-category":"nowplaying"})
    for li in liList:
        movie = {}
        title = li['data-title']
        duration = li['data-duration']
        region = li['data-region']
        director = li['data-director']
        actors = li['data-actors']
        img = li.find('img')
        thumbnail = img['src']

        movie['title'] = title
        movie['duration'] = duration
        movie['region'] = region
        movie['director'] = director
        movie['actors'] = actors
        movie['thumbnail'] = thumbnail

        movies.append(movie)
    return movies
# 数据存储
def save_data(data):
    with open('douban.json','w',encoding='utf-8') as fp:
        json.dump(data,fp,ensure_ascii=False)

if __name__ == '__main__':
    text = get_page()
    movies = parse_page(text)
    save_data(movies)
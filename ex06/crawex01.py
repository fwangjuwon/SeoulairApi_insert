# 크롤링

# python -m pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

html = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8")

soup = BeautifulSoup(html.text, 'html.parser')

weather_el = soup.select_one(".weather_graphic .temperature_text strong")

print(weather_el.get_text())

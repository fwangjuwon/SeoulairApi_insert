import requests
from datetime import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient


def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


# Mongo 연결
mongo = MongoClient("localhost", 20000)

# 리스트
list = []

for number in range(1, 21):
    dict = {}
    aid = format(number, '010')
    html = requests.get(
        f"https://n.news.naver.com/mnews/article/005/{aid}?sid=100")
    if(html.status_code == 200):

        print(number)
        soup = BeautifulSoup(html.text, 'html.parser')
        try:
            title_el = soup.select_one(
                ".media_end_head_title  .media_end_head_headline")
            company_el = soup.select_one(
                ".media_end_head_top_channel_layer_text > strong")
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dict['company'] = company_el.string
            dict['title'] = title_el.string.strip()
            dict['createdAt'] = date
            list.append(dict)
        except:
            title_el = soup.select_one(
                ".end_ct .end_tit")
            company_el = soup.select_one(
                ".end_ct .end_ct_area .press_logo > img")
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dict['company'] = company_el['alt']
            dict['title'] = title_el.string.strip()
            dict['createdAt'] = date
            list.append(dict)

mongo_save(mongo, list, "greendb", "navers")

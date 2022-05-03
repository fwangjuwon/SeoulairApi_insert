
import requests

list = []

aid = 1
while True:
    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{str(aid).zfill(10)}?sid=100")
        aid += 1
        print(html.status_code)
        if(html.status_code == 200):
            list.append(html.text)
    except Exception as e:
        pass

    try:
        if(html.status_code == 500):
            break
    except Exception as e:
        pass

print(len(list))

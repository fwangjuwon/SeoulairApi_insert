
import requests

list = []

aid = ["0000000001", "0000000002", "1000000003"]

for a in aid:
    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{a}?sid=100")
        print(html.status_code)
        if(html.status_code == 200):
            list.append(html.text)
    except Exception as e:
        pass

print(len(list))
print(list[0])

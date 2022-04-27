import json #C:\Users\Administrator\AppData\Local\Programs\Python\Python310\Lib   (라이브러리 임포트 경로)

json_str = '''
{
    "id": 1, "username": "cos", "password": "1234"
}
'''

#json -> dict
dic1 = json.loads(json_str)
print(dic1)
print(dic1["password"])

#dict -> json
dict_to_json = json.dumps(dic1)
print(dict_to_json)
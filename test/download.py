import requests
import json


# print(response.status_code)
# print("==================")
# print(type(response))
# print("==================")
# print(response.text)
# print("==================")
# print(response.json())
# print("==================")

# print(responseDict["RealtimeCityAir"]["list_total_count"])


def count():
    try:
        response = requests.get(
            "http://openapi.seoul.go.kr:8088/6b51714d6b6677613932755773536f/json/RealtimeCityAir/1/5/")

        if response.status_code == 200:
            responseDict = response.json()
            total = responseDict["RealtimeCityAir"]["list_total_count"]
            print("총 개수:", total)
            return total
        else:
            print('요청이 잘못되었습니다.')
    except Exception as e:
        print(e)


def info(total):
    try:
        response = requests.get(
            f'http://openapi.seoul.go.kr:8088/6b51714d6b6677613932755773536f/json/RealtimeCityAir/1/{total}')

        if response.status_code == 200:
            responseDict = response.json()
            list = responseDict["RealtimeCityAir"]["row"]
            return list
        else:
            print('요청이 잘못되었습니다.')
    except Exception as e:
        print(e)

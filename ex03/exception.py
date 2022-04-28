class MyException(Exception):
    pass


try:
    f = open("c:/hello.txt", "r")
    print(2/0)
except Exception as e:
    print(e)
finally:
    print("무조건 실행됨")

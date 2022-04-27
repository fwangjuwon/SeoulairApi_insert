# 함수(클래스 내부에 있는 것이 아닌 것들을 함수)

def add():
    print("더하기")


def minus():
    return 1


add()
n = minus()

print(n)


def multi(n1, n2=3):
    print(f"곱하기{n1}*{n2}")


multi(3, 2)

multi(2)

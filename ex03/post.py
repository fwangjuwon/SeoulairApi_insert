class Post:
    def __init__(self, username, password):
        self.username = username
        self.password = password


p = Post("ssar", "1234")

print(p.password)
print(p.username)
print(p.__dict__)  # 클라스를 dict로 바꾸면 json이다.

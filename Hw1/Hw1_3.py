Meta1 = type("Meta1", (), {'sur_name':'Kedesh' })
Meta2 = type("Meta2", (Meta1,), {})


class User(Meta2):
    pass

if __name__ == '__main__':
    user = User()
    print(user)
    print(user.sur_name)

# ex_23.py

id = "python"
passwd = "abcd"

id2 = input("id: ")
if id == id2:
    passwd2 = input("passwd: ")
    if passwd == passwd2:
        print("로그인")
    else:
        print("비밀번호가 틀립니다.")
else:
    print("그런 아이디는 존재하지 않습니다.")

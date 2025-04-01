# ex_25.py
pw = "1234"
success = False

for i in range(5):
    user_pw = input("PW: ")
    
    if user_pw == pw:
        print("로그인 성공")
        success = True
        break
    else:
        print("다시 입력하세요.")


# for i in range(5,0,-1):
#     user_pw = input("PW: ")
 
#     if user_pw == pw:
#         print("로그인 성공")
#         break
#     else:
#         print("비밀번호가 다릅니다.",f"남은기회:{i-1}")

# i == 0
# print("더 이상 시도할 수 없습니다.")

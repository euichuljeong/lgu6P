# ex_40.py

def Qr(x, y):
    q = 0
    r = 0
    while x >= y:
        x -= y
        q += 1
        # if x > 0:
        #     q += 1
        # elif x < 0:
        #     r = x + y
        #     break
        # else :
        #     q += 1
        #     break
    r = x
    return (q, r)

# x = int(input("나눠질 수를 입력하세요: "))
# y = int(input("나눌 수를 입력하세요: "))

# ret = Qr(x, y)
# print(f"({ret[0]}, {ret[1]})")
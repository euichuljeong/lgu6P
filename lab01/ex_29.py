# ex_29.py

n=5
# for i in range(n):
#     row=''
#     for j in range(n-1):
#         row+='*'
#     print(row)

for i in range(n):
    for j in range(n-i):
        print('*', end='')
    print()


for i in range(5,0,-1):
    for j in range(i):
        print('*', end="")
    print()
    
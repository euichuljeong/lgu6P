# ex_30.py

n = 8

# i : 0, 1, 2, 3, 4
# 공백: 4, 3, 2, 1, 0
# 별 : 1, 3, 5, 7, 9
for i in range(1,11,2):
    for j in range(n-i,-1,-2):
        print(' ', end="")

    for s in range(i):
        print('*', end="")

    print()

# for i in range(n):
#     star = ''
#     space = ''

#     for j in range(n-i-1):
#         space +=' '

#     for k in range(i*2+1):
#         star += '*'

#     row = space + star

#     print(row)





# for i in range(n):
#     print(f"{'*' * (i*2+1):^{n*2-1}}")
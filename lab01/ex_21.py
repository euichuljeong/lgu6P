# ex_21.py

# 5 x 1 = 5
# 5 x 2 = 10
# ...

n = int(input("원하는 단수: " ) )
for i in range (1,10):
    print(f"{n} x {i} = {n * i:>2}")
    # print(i*n)
    # i += 1

# ex_34.py

numbers = [10,4,5,-1,6,12,40]

n = numbers[1::2]

S = 0
for i in range(len(n)): # [0,1,2]
    S += n[i]
print(S)

S = 0
for i in n: #[4, -1, 12]
    S += i
print(S)

print( sum(n) )

print( max(numbers) )

maximum = numbers[0]
for i in numbers[1:]:
    if i > maximum:
        maximum = i
    # else:
    #     pass
print(maximum)
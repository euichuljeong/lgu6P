# ex_41.py

def mean(l):
    # l : List[int or float]
    # for x_k in l:
    #     S += x_k
    for k in range(len(l)):
        x_k = l[k]
        S += x_k
    
    N = len(l)
    m = S / N

    return m

avg = mean([1,2,3,4,5,6])
print(avg)

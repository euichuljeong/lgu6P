# ex_42.py

def mean2(X):
    # A=0
    # B=0
    #    A   B
    A = [0,  0]
    for k in range(len(X)):
        for i in range(len(X[0])):
            A[k] += X[k][i]

                
    N = len(X[0])
    m = (A[0] / N) , (A[1] / N)

    return m

X = [[78, 80, 95, 55, 67, 43], 
     [45, 67, 90, 87, 88, 93]]

m = mean2(X)
print(m)

# AVG = [ round(mean(x),2) for x in X]

# AVG = []
# for x in X:
#     m = mean(x)
#     print(m)
#     AVG.append( round(m,2))

# print(AVG)
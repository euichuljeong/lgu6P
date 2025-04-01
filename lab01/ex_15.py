# ex_15.py

x = float(input("x: ") )
y = float(input("y: ") )
a = float(input("a: ") )


A = 1/(a*2.506)
B = -((x-y)**2/(2*a**2))
C = 2.718**B

print(A*C)

# ex_str.py

s = "Hello Python"
print(s)

s = 'Hello Python'
print(s)

s = "Hello \"EASY\" Python"
print(s)

s = 'Hello "EASY" Python'
print(s)

s = 'Hello,\n "EASY" Python'
print(s)
print(type(s))

s = """Hello,
       "EASY"python
"""
print(s)

##########################
# F-string
##########################
a = 10.0
b = 20.0
c = a * b
# print('c:', c, 'SUCCESS')
# print(f"c: {c} SUCCESS")
print(f"{a:5.2f} x {b:5.2f} = {c:f}")


d = 5.2
e = 21.234
f = d * e
print(f"{d} x {e} = {f:.3f}")

a = "hello"
print(f"{a:_^15}")

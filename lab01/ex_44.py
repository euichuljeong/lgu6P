# ex_44.py

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "오류: 0으로 나눌 수 없습니다"
}

# 두 수와 연산자를 사용자로부터 입력받고
# 입력된 연산을 operations를 이용하여 수행하기
# print( operations['+'](10,2))
x = float(input("첫 번째 숫자를 입력하세요: "))
y = float(input("두 번째 숫자를 입력하세요: "))
op = input("연산자를 입력하세요 (+,-,*,/): ")

if op in operations.keys(): # ['+', '-', '*', '/']:
    result = operations[op](x, y)
    print(result)
else:
    print("올바른 연산이 아닙니다.")
# print(x, op, y, '=', operations[op](x,y))
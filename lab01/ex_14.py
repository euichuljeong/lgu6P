#ex_14.py

pi = 3.14

radius = float(input("원의 반지름을 입력하세요: ") )

area = pi*radius*radius
circum = 2 * pi * radius
d = radius*2
area = round(area, 1)

print(f"반지름이 {radius}인 원의 면적은 {area}입니다.\n이 원의 둘레는 {circum}입니다.\n이 원의 지름은 {d}입니다.")
# print(f"면적 {area}, 둘레 {circum}, 지름 {d}")

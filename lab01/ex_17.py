# ex_17.py

height = float( input("키(m): " ) )
weight = float( input("몸무게(kg): " ) )

BMI = round(weight / height**2, 3)

if BMI >= 25:
    print('비만', 'BMI: ',BMI)
elif BMI >=23:
    print('과체중', 'BMI: ',BMI)
elif BMI >=18.5:
    print('정상', 'BMI: ',BMI)
else:
    print('저체중', 'BMI: ',BMI)
# if BMI < 18.5:
#     print('저체중', 'BMI: ',BMI)
# elif 18.5 <= BMI < 23:
# elif 18.5 <= BMI and BMI < 23:
    # print('정상', 'BMI: ',BMI)
# elif 23 <= BMI < 25:
# elif 23 <= BMI and BMI < 25:
#     print('과체중', 'BMI: ',BMI)
# else :
#     print('비만', 'BMI: ',BMI)


# a = -3

# if a > 0 :
#     print("positive")
# elif a < 0 :
#     print("negative")
# else :
#     print("zero")

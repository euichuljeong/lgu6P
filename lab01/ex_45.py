# ex_45.py
import math
def mean(l): # 리스트 평균값 구하는 함수
    # l : List[int or float]
    S = 0 # 변수 기본값 0으로 설정
    # for x_k in l:
    #     S += x_k
    for k in range(len(l)): # k는 리스트 안에 숫자들
        x_k = l[k] # 리스트 안에 모든 숫자들
        S += x_k # 리스트 안에 모든 숫자들의 합
    
    N = len(l) # 리스트 내 숫자 갯수
    m = S / N # 리스트안에 숫자들의 합 나누기 갯수 = 평균

    return m # 평균값 저장

def std(l):
    m = mean(l) # m = 평균값 구하는 함수의 결과값
    # S = 0
    # for x_k in l:
    #     S += (X_k - m)**2
    # var = S / len(l)
    var = mean([ (x_k - m)**2 for x_k in l ])
    sigma = math.sqrt(var)
    return sigma
# (데이터 - 평균) 을 제곱해, 전부 더해, 숫자하나 생김, 데이터 양으로 나눠, 거기 루트씌워


if __name__ == '__main__': # 테스트 코드
    print('TEST CODE')
    L = [1,2,3,4,5,6,7,8,9,10]
    print(std(L))
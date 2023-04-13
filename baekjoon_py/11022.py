# 리스트
t = int(input()) # 몇 개의 식을 받을지
sum = list() #리스트 3개 선언
x = list()
y = list()
for i in range(0,t): # 숫자 두 개 입력받고 x,y,sum 리스트에 추가
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    sum.append(a+b)
for i in range(0,t): # 문제 조건대로 출력
    print(f"Case #{i+1}: {x[i]} + {y[i]} = {sum[i]}")
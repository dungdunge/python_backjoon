numbers = list() # list 선언
for i in range(10): # 10번 반복
    n = int(input()) # 정수 입력받고
    numbers.append(n%42) # list에 42로 나눈 나머지값 추가
numbers = list(set(numbers)) # list를 set으로 중복 요소 제거
print(len(numbers)) # 중복 제거한 list 개수 출력
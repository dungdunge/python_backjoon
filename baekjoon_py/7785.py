n = int(input()) # 입력할 출입 기록 수
dic=dict() # dictionary 선언
for i in range(n): # 입력받은 key, value 값 dic에 저장
    a, b = input().split() # 공백을 기준으로 나누는 split
    dic[a]=b # dictionary에 a, b 추가
    if b == 'leave' : # value가 'leave'이면 key 삭제
        del dic[a]

for x in sorted(dic.keys(), reverse=True): # 역순으로 출력
    print(x)
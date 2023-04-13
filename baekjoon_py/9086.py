# 리스트
num = int(input()) # 테스트 케이스 개수 입력
test_case = list() # 문자열 입력받을 리스트
cases = list() # 입력받은 문자열 처음+끝을 저장할 리스트
for i in range(0,num): # 3번 문자열 입력받고 문자하나씩 리스트로 나눠줌
    a = input()
    test_case = list(a.strip(""))
    # 출력할 리스트에 저장 append는 stack 쌓는 것처럼 하는거라 
    # 선언 안된 cases 리스트에 추가 가능
    cases.append(test_case[0] + test_case[len(test_case)-1])
for i in range(num): # 출력
    print(cases[i])
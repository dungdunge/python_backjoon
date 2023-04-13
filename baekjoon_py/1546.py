import sys
x = int(input())
if (x<=1000):
    pass
else :
    sys.exit("입력받을 점수 개수 조건 안맞음 = 종료")
grade = list(map(float, input().split()))
# 점수값 조건 지정, 안맞으면 종료
def check_jogun(list): 
    count = 0
    for i in range(0,len(list)):
        if(list[i]>100 or list[i]<0):
            count = count + 1
    return count
# 입력받은 점수 list 중 MAX값 찾기
def MAX_find(list): 
    MAX = list[0]
    for i in list:
        if i > MAX:
            MAX = i
    return MAX
# 문제의 조건대로 점수 초기화
def grade_reset(list, MAX):
    for i in range(0, len(list)):
        list[i] = list[i]/MAX*100
# 초기화한 점수를 이용해 평균 구하기
# 소수점 6자리까지만 retrun
def ave_grade(list):
    ave = 0
    for i in list:
        ave += i
    ave = ave / len(list)
    return round(ave,6)
if(check_jogun(grade) == 0):
    pass
else:
    sys.exit("점수 조건 안맞음 - 종료")
MAX = MAX_find(grade)
grade_reset(grade, MAX)
print(ave_grade(grade))
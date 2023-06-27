# 파이썬 완천기초
# 파이썬 제어문
# IF 문

print(type(True)) # 0 이 아닌 수, 'ab', [1,2,3], (1,2,3,4), {1:2, 3:4}
print(type(False)) # 0 , "", [], (), {}, ...

# 예1

if True:
    print("Good")

if False:
    print("Bad")

# 예2
if False:
    print("bad")
else:
    print("Good")
print("===============")

# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

# 양 변이 같은 경우 참
print(x == y)

# 양 변이 다른 경우 참
print(x != y)

# 왼쪽이 클 때 참
print(x>y)

# 왼쪽이 크거나 같을 때 참
print(x>=y)
# 오른쪽이 클 때 참
print(x<y)
# 오른쪽이 크거나 같을 때 참
print(x<=y)

# 예3
print("===============")

city2 = "Seoul"
if city2:
    print("you are in:",city2)
else:
    print("Please enter your key")

# 예4
print("===============")
# and or not 

a = 75
b = 40
c = 10

print('and', a > b and b > c) # a>b>c
print('or', a > b or b > c)
print('not', not a > b)
print('not', not b > c)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1 : ', 3+12 > 7+3)
print("e2 : ", 5+10 * 3 > 7 + 3 * 20)
print("e3 :", 5+10 > 3 and 7 + 3 == 10)
print("e4 :", 5+10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

# 예4
# 복수의 조건이 모두 참일 경우에 실행
if score1>=90 and score2 == 'A':
    print("Pass")
else:
    print('Fail')


# 예5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == "vip" or id2 == "admin":
    print("관리자 입장")

if id2 == "admin" and grade == "platinum":
    print("최상위 관리자")


# 예6
# 다중 조건문

num = 90

if num >= 90:
    print("Grade : A")
elif num >= 80:
    print("Grade : B")
else:
    print("과락")

# 예7
# 중첩 조건문

grade = 'A'
total = 95

if grade == 'A':
    if total >=95:
        print("장학금 100%")
    elif total >= 80:
        print("장학금 80%")
    else:
        print("X")
else:
    print("장학금 없음")

# in, not in

q = [10,20,30]
w = {70,80,90,100}
e = {"name":"Lee","City":"Seoul","Grade":"A"}
r = (10,12,14)




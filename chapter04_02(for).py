# 파이썬 반복문
# FOR 실습

# 코딩의 핵심
# for in <collection>
# < Loop boudy>

for v1 in range(10):
    print(v1)

for v2 in range(1, 11):
    print(v2)

for v3 in range(1,11,2):
    print(v3)

print("================")
sum1 = 0
for v in range(1,1001):
    sum1 +=v
print(sum1)

print(sum(range(1,1001)))
print('1 ~ 100 4의 배수의 합 : ',sum(range(4,1001,4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['kim', 'park', 'cho', 'Lee', 'choi', "yeo"]
for name in names:
    print(name)

# 예제2
lotto_numvers = [11,19,21,28,36,37]
for n in lotto_numvers:
    print("Current number : ", n)


# 예제3
word = "Beautiful"

for s in word:
    print('word : ', s)

# 예제 4

my_info = dict(
    name = "Lee",
    Age = 33,
    City = "seoul"

)

for my in my_info:
    print(my)

for my in my_info.values():
    print(my)


# 예제 5
name = "FineAppLE"
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2 ,33, 15, 34, 36, 38]

for n in numbers:
    if n == 34:
        print('find : 34!')
        break
    else:
        print('Not Found!',n)

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:
        continue
    print("curent Type:", type(v))
    print("multiply byt 2", v * 3)
    print(True * 3)

print(">>>>>>>>>>>>>>>>>>")
# for - else

numbers = [14, 3, 4, 7, 10, 24, 17, 2 ,33, 15, 34, 36, 38]

for num in numbers:
    if num == 3:
        print("Found : 24")
        break
else:
    print("Not Found : 24")

## 구구단 출력

for i in range(2,10):
    for j in  range(1,10):
        print(i,'*',j,"=",i*j, end=', ')
    print()

print(">>>>>>>>>>>>>>>>>>")
## 변환 예제
name2 = "Aceman"

print('Reverse', reversed(name2))
print('Reverse', list(reversed(name2)))
print('Reverse', tuple(reversed(name2)))
print('Reverse', set(reversed(name2))) # 순서 x2





# 파이썬 완천기초
# 파이썬 집합
# 집합(set) 자료형(순서X)

# 선언
a = set()
b = set([1, 2, 3, 4,4 ,4 ])
c = set([1,4,5,6])
d = set([1, 2, 'pen'])
e = {'foo', 'bar', 'baz', 'fppp', 'qux'}
f = {42, 'foo', (1,2,3,), 3.14159}

print('a - ', type(a), 2 in a )
print('a - ', type(b), 2 in b)
print('a - ', type(c), c)
print('a - ', type(d), d)
print('a - ', type(e), e)
print('a - ', type(f), f)
print(a)

# 튜블 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t),t)
print('t - ',t[0:3])
print('=========================')

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l=', l)
print('l2=', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print('=========================')

# 집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print('s1 & s2 >:' , s1 & s2)
print('s1 & s2 >:' , s1.intersection(s2))
print('s1 | s2 >:' , s1 | s2)
print('s1 & s2 >:' , s1.union(s2))
print('s1 - s2 >:' , s1 - s2)
print(s1.difference(s2))
print('=========================')

# 중복 원소 확인
print('s1 & s2', s1.isdisjoint(s2))

# 부분 집합 확인
print(s1.issubset(s2)) #  포함인지
print(s1.issuperset(s2)) # 전부 포함인지

# 추가 & 제거
s1 = set([1,2,3,4])
s1.add(5)
print(s1)

s1.remove(2)
print(s1)

# 파이썬 완천기초
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서X 키 증복X, 수정O, 삭제O)


# 선언
a = {'name': 'kim', 'phone':'01033337777', 'birth': '870514'}
b = {0: 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'NiceMan',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('Name' , 'NiceMan'),
    ('City' , 'Seoul'),
    ('Age' , 33),
    ('Grade' , 'A'),
])

f = dict(
    Name = 'niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
print('a - ',a['name']) # 존재하지 않을 경우 에러 발생
print('a - ', a.get('name')) # 존재하지 않을 경우 none 출력
print('b - ', b.get(0)) # 존재하지 않을 경우 none 출력
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ',a)
a['rank'] = [1,2,3]
print(a)
print('a - ',len(a))
print()

# dict_key, dict_value, dict_item : 반복문(__iter__)에서 사용 가능

print('a - ',list(a.keys()))
print('a - ',a.values())
print()

print('a - ',a.items())
print()

print('a - ', a.pop('name'))
print('a - ', a)

print('c - ', c.pop('arr'))
print('c - ', c)

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print()

print('a - ', 'birtht' in a)

# 수정
a['test'] = 'test_dict'
print(a)
a['address'] = 'dj'
print(a)

a.update(birth='910914')
print(a)
temp = dict( address = 'Busan')


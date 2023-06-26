# print 사용법(2023년 추가)
#파이썬 3가지 print Formating
# 자주 나오는 질문

"""
참고 : ESCAPE 코드
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
'''
"""

### 3가지 Format Practices
x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, num = %d ' %(n,text,(x+y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, num = {sum}'.format(n=n,s=text,sum=(x+y))
print(ex2)

# 출력3
ex3 = f'n = {n}, s={text}, sum={x+y}'
print(ex3)

# 구분기호
m= 100000000
print(f'm = {m:,}')

print()

# 정렬
# ^ : 가운데 정렬 , < : 왼쪽 정렬 , > : 오른쪽 정렬
t=20

print(f't : {t:^}')
print(f't center  : {t:^10}')
print(f't center  : {t:<10}')
print(f't center  : {t:>10}')

print()

print(f't center  : {t:*^10}')
print(f't center  : {t:#<10}')
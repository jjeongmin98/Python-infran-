# 파이썬 완천기초
# 파이썬 반복문
# while 실습

# while <expr>:
# <statement(s)>

# 예제1

n = 5
while n > 0:
    n = n - 1
    print(n)
print(">>>>>>>>>>>>>>")
# 예제 2 
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

print(">>>>>>>>>>>>>>")


#예제 3
# break, continue
n = 5
while n > 0:
    n -=1
    if n == 2:
        break
    print(n)
print('Loop Ended.')
print(">>>>>>>>>>>>>>")

# 예제 4
m = 5
while m > 0:
    m -=1
    if m == 2:
        continue
    print(m)
print("Loop Ended")

# if 중첩
# 예제5
i = 1
print(">>>>>>>>>>>>>>")
while i<= 10:
    print("i:",i)
    if i == 6:
        break
    i += 1
print(">>>>>>>>>>>>>>")

# 예제6
n = 10
while n > 0:
    n -=1
    print(n)
    if n== 5:
        break
else:
    print("else out")

# 예제 7
a = ["foo", "bar", "bax", "quz"]
s = "quz"
print(">>>>>>>>>>>>>>")

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, "not Found in list.")
print(">>>>>>>>>>>>>>")

# 무한 반복
# while True:
# print("Foo")

# 예제 8
a = ["foo", "bar", "bax", "quz"]

while True:
    if not a:
        break
    print(a.pop())


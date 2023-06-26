# 파이썬 완천기초
# 문자형
# 문자형 중요

# 문자열 생성
str1 = "I Am Python"
str2 = "Python"
str3 = "How are you?"
str4 = "Thank you"

print(type(str1),type(str2),type(str3),type(str4),)
print(len(str1),len(str2),len(str3),len(str4),)
print()

# 빈 문자열
str1_t1 = ""
str2_t2 = str()
print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm Boy

print("I'm Boy")
print('I\'m Boy')

print('a \t b')
print('a \n b')

escape_str1 = "Do you habe a \"retro game\"?"
print(escape_str1)

# 탭, 줄 바꿈
t_s1 = "click \t start"
t_s2 = "New Line \b Check"
print(t_s1)
print(t_s2)
print()


# Raw String
raw_s1 = r'D\pthon\test'
print(raw_s1)

# 멀티라인 입력
multi_Str = \
"""
문자열
멀티라인 입력
테스트
"""
print(multi_Str)

# 문자열 연산
str_01 = "python"
str_02 = "Apple"
str_03 = "How are you doing"
str_04 = "Seoul Daejeon Busan Jinju"

print(str_01 * 3)
print(str_01 + str_02)
print('y' in str_01)
print('z' in str_01)
print('P' not in str_02) # 대소문자를 구별한다

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endwith, isalpha...)

print('Capitalize :', str_01.capitalize()) # 첫 글자만 대문자
print('endwith :', str_02.endswith("e")) # 마지막 문자 확인
print("replace : ", str_01.replace("thon", "Good"))
print("sorted:", sorted(str_01))
print("split : ", str_04.split(' '))

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i,end="")

print()


# 슬라이싱 
str_sl = "Nice Python"

print(len(str_sl))

# 슬라이싱 연습
print(str_sl[0:3]) # index 0, 1, 2
print(str_sl[5:]) # [5:11]
print(str_sl[:len(str_sl)]) # str_sl[0:11]
print(str_sl[:len(str_sl)-1]) # str_sl[0:10]
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])

# 아스키 코드
a ='z'

print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로


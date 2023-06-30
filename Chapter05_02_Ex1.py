# 파이썬 사용자 입력
# input 사용법
# 기본 타입(str)

# try:
#     n = int(input("Enter a number : "))
#     print("ok Your number is : ", n)
# except ValueError:
#    print("This is not a number")

# 예제 2 -> 옳바른 값 입력 완료 까지 지속

while True:
    try:
        n = int(input("Enter a number : "))
        print("ok Your number is : ", n)
        break
    except ValueError:
        print("This is not number")
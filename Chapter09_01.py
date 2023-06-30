# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기모드 w, 추가 모드 , 텍스트모드 t, 바이너리 모드 b
# 상대 경로('../, ./'), 절대 경로("C:\Django/example..")

# 파일 읽기(Read)
# 예제1

# f = open("./resource/it_news.txt", 'r', encoding  = "UTF-8")
# # 속성 확인
# print(dir(f))
# # 인코딩 확인
# print(f.encoding)
# # 파일 이름
# print(f.name)
# # 모드 확인
# print(f.mode)
# # 반드시 close
# f.close

# 예제2
with open("./resource/it_news.txt", 'r', encoding  = "UTF-8") as f:
    c = f.read()
    print(c)
    print(list(c))
    print(list(c))

print()

# 예제3
# read() : 전체 읽기, read(10) : 10byte
with open("./resource/it_news.txt", 'r', encoding  = "UTF-8") as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)

print()

# 예제4
# readline : 한 줄 씩 읽기

with open("./resource/it_news.txt", 'r', encoding  = "UTF-8") as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

# 예제 5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장

with open("./resource/it_news.txt", 'r', encoding  = "UTF-8") as f:
    lines = f.readlines()
    print(line)
    print()
    for c in lines:
        print(c, end="")

# 파일 쓰기 (Write)
with open("./resource/contents.txt", 'w', encoding  = "UTF-8") as f:
    f.write("I love python\n")

# 파일 쓰기 (Write)
with open("./resource/contents.txt", 'a', encoding  = "UTF-8") as f:
    f.write("I love python\n")

# 예제3
# writeLines : 리스트 -> 파일
with open("./resource/contents.txt", 'a', encoding  = "UTF-8") as f:
    list = ["Orange\n", "Apple\n", "Banana\n"]
    f.writelines(list)

# 예제4
with open("./resource/contents.txt", 'a', encoding  = "UTF-8") as f:
    print("test Text Write!!", file=f)
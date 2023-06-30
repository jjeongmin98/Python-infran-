
# 행맨 미니 게임 제작
# 기본 프로그램 제작 및 테스트

import time
import csv
import random
import sound
# 처음 인사
name = input("What is your name? : ")
print("Hello", name ," Wlecome to hangman game!!!")
time.sleep(1)
print("Start Loading...")
time.sleep(0.5)

#csv 단어 리스트 선언
words = []
# 문제 csv 파일 로드
with open("./resource/word_list.csv", "r", encoding="UTF-8") as f:
    reader = csv.reader(f)
    #헤더 필요 없음
    next(reader)
    for c in reader:
         words.append(c)

# 섞기
random.shuffle(words)
# 정답 단어
word = random.choice(words[0])



# 추측 단어
guesses= ""
# 기회
turn = 5

# 핵심 while
# 찬스 카운터가 남아있을 경우
while turn > 0:
    # 실패 횟수(단어 매치 수)
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses :
            # 추측 단어 출력
            print(char,end=" ")
        else:
            print("_" , end=" ")
            failed +=1
            
        # 단어 추측이 성공한 경우
    if failed == 0:
            print("Answer!!!!")
            break


    # 추측 단어 문자 단위 입력
    print()
    guess = input("Guess a Character.")

    # 단어 더하기
    guesses += guess

    if guess not in word:
        turn -=1
        # 오류 메시지
        print("Oops! Wrong")
        # 남은 기회 출력
        print("You have", turn, "more Guess!!")
        if turn == 0:
            print("Bye~!!")






#python file 실행 > 터미널에 python ~~.py
# 저장 = ctrl + s

greeting = '반갑습니다.'
#greeting이라는 변수에 반갑습니다.라는 문자열을 저장.

player = 3

#3명 모두에게 인사를 하려면?

def bot():
    player = 5
    while player > 0:
        print(greeting)
        player = player - 1

player = 3

for _ in range(player):
    print('hi')

# 커서 범위 저장후 alt 누르고 방향키 누르면 해당 코드들이 이동함

#built in function > ex= for while
#non-built-in function > import 해오는 서랍안 가위 풀 // 기본적으로 파이선에 다 포함되어 있음
#trd party > python안에 없는 곳에서 가져옴
#pip python 환경의 쿠팡, pip 야 나 ~ 설치할거야 해줘~

#과목 평가 25일 내장함수 수업 x > 본인이 구현할수 있어야함 google python 3.9버전에서 내장함수(built-in) 기능 알기.

# 함수나 변수 등을 모아놓은 파일 = 모듈

#함수 만들기 > def 
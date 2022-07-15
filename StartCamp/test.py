#방법 1 import hello

# print(hello.player)


#방법 2

from hello import greeting, player
from hello import bot

print(greeting)
print(player)

bot()

#밑 결과 저렇게 나오는 경우 > 불러올떄 한번 실행 시켜서 print 함수들 실행됨, 그래서 모듈로 쓸땐 모듈안의 함수가 쓸데없는것이 없어야함. 지역변수 > 함수내에서만 존재, 전역변수 = ?
# scope > LEGB

#python을 가지고 외부에 요청~~ 라이블러리 = requests
#pip install requests
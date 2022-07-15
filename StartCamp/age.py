import re
import requests

url = 'https://api.agify.io/?name=viktor'
response1 = requests.get(url)
response = requests.get(url).json()
print(response)
print(type(response))
name = response['name']
age = response['age']
count = response['count']

print( '이름이' + name + '인 사람의 나이는' + str(age) + '입니다.')
#스테이더스 코 드??  response [200] 이런것 처럼 2가뜨면 성공적으로 결과값이 나왓다는 뜻.

#api = application programming interface > 컴퓨팅 처리를 쉽게 해주는 기능.
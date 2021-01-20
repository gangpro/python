# numbers.txt의 내용을 뒤집어서 저장한다.
# 1. line 불러오기
with open('numbers.txt', 'r') as f:
    lines = f.readlines()
    #print(lines)

# 2. list 뒤집기
lines.reverse()

with open('numbers.txt', 'w') as f:
    for line in lines:
        # String.strip() : 문자열의 처음과 끝의 공백을 지워주는 매서드
        # rstrip() 오른쪽 공백 삭제
        # lstrip() 왼쪽 공백 삭제
        f.write(line.rstrip() + '\n')


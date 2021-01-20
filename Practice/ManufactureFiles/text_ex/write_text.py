# 파일을 여는 함수 open
# 1번째 매개변수로 파일 이름이 옴
# 2번째 매개변수로 open option
#   r : 읽기 - read
#   w : 쓰기 - write (overwrite)
#   a : 추가 = append

# open 한 팡리 객체를 반환한다.


# 방법 1
f1 = open('mulcam1.txt', 'w')
f1.write('Happy Hacking 1\n')
f1.write('Happy Hacking 2\n')
f1.write('Happy Hacking 3\n')
f1.close()

# 방법 2
f2 = open('mulcam2.txt', 'w')
for i in range(10):
    f2.write(f'Happy Hacking {i+1} \n')
f2.close()


# 방법 3
'''
python에서 with 구문은 '컨텍스트 매니저' 이다.
with 블럭을 통해 명시적으로 파일을 불러서 작업하는 코드 블럭을 만들 수 있다.
with 블럭이 종료되면 자동으로 파일을 닫는다.
'''
with open('mulcam3.txt', 'w') as f3:
    for i in range(10):
        f3.write(f'Happy Hacking {i + 1} \n')
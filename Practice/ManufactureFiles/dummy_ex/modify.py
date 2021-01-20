# 지원자_000_홍길동 => 합격자_000_홍길동 으로 바꿔보기
# abc.replace('b', 'e') : b를 e로 변경. 즉, aec로 변경됨.

import os

filenames = os.listdir('.')
#print(filenames)

for filename in filenames:
    txt = os.path.splitext(filename)[-1]
    #print(txt)
    if txt == '.txt':
        newfilename = filename.replace('지원자', '합격자')
        os.rename(filename, newfilename)

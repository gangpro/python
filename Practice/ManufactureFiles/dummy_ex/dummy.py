import os  # 운영체제 인터페이스
import random

# os.system('git status')  # 터미널 커멘드를 작성하여 실행시킬 수 있다.

family = ['김', '이', '박', '최', '황', '오', '강', '한', '제갈 ', '하', '정', '송', '현', '손', '조', '문', '허']
given = ['길동', '진웅', '민준', '소미', '수진', '지은', '동해', '민태', '준호', '세정', '지훈', '성우', '성원', '수민', '무지']

for i in range(500):
    cmd = f"touch {str(i + 1)}_{random.choice(family)}{random.choice(given)}.txt"
    print(cmd)
    os.system(cmd)

# '000_홍길동' 기존 파일들 앞에 '지원자_'를 붙여보기


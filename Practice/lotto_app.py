# 1 ~ 45의 숫자중에서 중복되지 않는 랜덤 6개 숫자를 뽑아서 출력하는
# 앱을 만들어 보세요!
# ex) '행운의 숫자는 1, 2, 3, 4, 5, 6 입니다!'
import random

numbers = list(range(1, 46))    #[1,2, ... 45]
lotto = random.sample(numbers, 6)
lotto.sort()

print(f"오늘의 행운의 숫자는 {lotto} 입니다!")

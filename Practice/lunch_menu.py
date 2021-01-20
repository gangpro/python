import random

# menu 리스트를 만들어주세요.
menu = ["멀캠 구내식당", "삼백집", "시골집", "양자강", "순남시레기", "백수산"]
phonebook = {"멀캠 구내식당" : "000-000",
             "삼백집" : "111-111",
             "시골집" : "222-222",
             "양자강" : "333-333",
             "순남시레기" : "444-444",
             "백수산" : "555-555"}

choice = random.choice(menu)
print("오늘의 추천 점심 식당은 " + choice + "입니다.")  # 기존 방식
print(f"오늘의 추천 점심 식당은 {choice}입니다.")  # fString 사용
print(f"식당 전화 번호 : {phonebook[choice]}")  # fString 사용

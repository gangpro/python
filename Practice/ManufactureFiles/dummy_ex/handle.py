import os

# os.chdir('폴더 경로') : 지정한 폴더로 이동하게 하는 method
# os.listdir('폴더 경로') : 폴더에 저장된 전체 파일목록을 list로 반환
# os.rename('기존 파일명', '바꿀 파일명') : 파일이름 변경
# os.path.splitext('파일이름') : 파일 경로와, 확장자를 분리하여 반환
# ‎⁨MAC⁩/Users⁩/kang⁩/Documents⁩/PycharmProjects⁩/TIL⁩/ManufactureFiles⁩/dummy_ex

# test
# os.path.splitext(r'') : r 의미 : escape 문자를 무시하겠다.
# filename = os.path.splitext(r'MAC⁩/Users⁩/kang⁩/Documents⁩/PycharmProjects⁩/TIL⁩/ManufactureFiles⁩/dummy_ex/dummy.py')
# print(filename)  # 결과값 : ('MAC\u2069/Users\u2069/kang\u2069/Documents\u2069/PycharmProjects\u2069/TIL\u2069/ManufactureFiles\u2069/dummy_ex/dummy', '.py')

# os.chdir('/MAC⁩/Users⁩/kang⁩/Documents⁩/PycharmProjects⁩/TIL⁩/ManufactureFiles⁩/dummy_ex')
os.chdir('/MAC/Users/kang/Documents/PycharmProjects/TIL/ManufactureFiles/dummy_ex')
filenames = os.listdir('.')
print(filenames)

for filename in filenames:
    txt = os.path.splitext(filename)[-1]  # 가장 마지막에 있는 경로가 확장자로 인식
    # print(txt)
    if txt == '.txt':
        os.rename(filename, f'지원자_{filename}')  # 앞에 '지원자_'를 붙인다.
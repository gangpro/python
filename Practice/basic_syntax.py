# Basic Sintax
print('안녕하세요')
print('저는 홍길동입니다.')
print('만나서 반갑습니다.')



# ''' -> 3개를 이어서 쓰면 줄바꿈 가능
print('''
안녕하세요.
저는 홍길동입니다.
만나서 반갑습니다.
''')



# Range
# 숫자의 범위를 가지고 있다.
print(range(5))  # => range(0,5)



# List 형 변환
print(list)  # => <class 'list'>
a = list(range(5))
print(a)  # => [0, 1, 2, 3, 4]



# Range를 이용한 반복문
for i in range(3):
    print(i)



# List
# 배열이다. 여러개의 멤버변수를 가질 수 있으며 index를 통한 접근이 가능하다. 다른 언어에서는 Array이라 불린다.
numbers = [0, 1, 2, 3]
print(numbers[0])  # => 0
print(numbers[-1])  # => 3
print('----------------')



# sorted() 함수는 배열을 정렬해주지만 원본을 바꾸지 않는다.
numbers = [3, 1, 2]
print(numbers)  # => [3, 1, 2]
print(sorted(numbers))  # => [1, 2, 3]
print(numbers)  # => [3, 1, 2]


# .sort() 함수는 원본을 바꾼다.
print(numbers.sort())   # => None
print(numbers)  # => [1, 2, 3]



# Dictionary
# key와 value로 이루어진 자료 구조
# 다른 언어에서는 map, object라고 불린다.
phonebook = {
    '중국집' : '123-456',
    '일식집' : '789-012',
    '한식집' : '111-222'
}

print(phonebook['중국집'])  # => 123-456




# 한번에 주석처리
# command + /

class Person:
    def __init__(self, name):
        self.name = name

    def myname(self):
        print(f'안녕하세요. 제 이름은 {self.name}입니다.')

    @classmethod
    def greeting(cls):
        print('안녕하세요.')

iu = Person('IU')
print('사람(클래스) 안녕하세요.')
Person.greeting()
print('아이유(인스턴스) 안녕하세요.')
iu.greeting()
iu.myname()
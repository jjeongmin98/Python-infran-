# 파이썬 클래스
# OOP(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 코드에 올라가서 활용할수 있는 그 대상
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1

class Dog(object): # object 상속
    # 클래스 속성
    species = "firstdog"

    # 초기화 / 인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
# 인스턴스화 시킨것들은 전부 다른 id를 가지고 있다.
a = Dog("miky", 2)
b = Dog("baby", 3)
c = Dog("baby", 3)

# 비교
print(a == c, id(a), id(c))


# 네임 스페이스
print("dog1", a.__dict__)
print("dog2", b.__dict__)


# 인스턴스 속성 확인
print("{} is {} and {} is {}".format(a.name, a.age, b.name, b.age))

if a.species == "firstdog":
    print("{0} is a {1}".format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# 예제 2
# self의 이해
class SelfTest(object):
    def func1():
        print("func1 called")
    def func2(self):
        print(id(self))
        print("Func2 called")

f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2()

# self 는 인스턴스를 요구한다 즉  func1이 안나오는 이유는 id 값을 보냈는데 쓰지 않기 때문이다

SelfTest.func1()
# 상단에서는 매개변수를 넣어주지 않기 때문에 func1 에서는 오류가 나오지 않으나 func2 에서는 오류가 나오게된다.

SelfTest.func2(f)
# 상단처럼 id 값이 들어가게 된다면 오류 없이 정상적으로 실행하게 된다.


# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num +=1

    def __del__(slef):
        Warehouse.stock_num -=1

user1 = Warehouse('Lee') # 인스턴스화
user2 = Warehouse("cho")

print(Warehouse.stock_num)
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print("Before ",Warehouse.__dict__)
print(user1.stock_num) #stock_num은 전체가 공유하기 때문에 인스턴스에서 없을경우 클래스에서 확인한다
print()
del user1
print("After", Warehouse.__dict__)

# 예제4

class Dog(object): # object 상속
    # 클래스 속성
    species = "firstdog"

    # 초기화 / 인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)
    
# 인스턴스 생성

c = Dog("juily", 4)
d = Dog("Marryt", 10)

# # 메소드 호출
print(c.info())
print(c.speak("wal wal"))
print(d.speak("wang wang"))
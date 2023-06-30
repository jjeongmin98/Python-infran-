# 파이썬 함수 및 중요성
# 파이선 함수식 및 람다(Lamda)

# 함수 정의 방법
# def function_name(parameter):
# 인프런 함수형 프로그래밍 학습 요망
# code

# 예제1
def  firts_func(w1):
    print("Hello, ",w1)

word = "Good boy"
firts_func(word)

# 예제2
def return_function(w1):
    value = "Hello " + str(w1) 
    return value

x = return_function("Goody boy2")
print(x)

# 예제3 (다중 반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1,y2,y3

x, y, z = func_mul(10)

print(x, y, z)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1,y2,y3    

q = func_mul2(20)
print(type(q), q)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1,y2,y3]    

l = func_mul2(20)
print(type(l),l,set(l))

# 딕셔너리 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return dict(v1= y1,v2= y2,v3= y3)

d = func_mul2(20)
print(type(d),d,set(d))
print(d,d.get('v2'), d.items(), d.keys())
print(">>>>>>>>>>>>>")

# 중요
# *args, **Rwargs

# *args(언팩킹) > 튜플
def args_func(*args): # 매개 변수 명은 자유
    for i,v in enumerate(args):
        print("result : {}".format(i),v)
    print("---------")

args_func("Le")
args_func("Le", "park")
args_func("Le", "park", "kim")
print(">>>>>>>>>>>>>")

# **kwargs(언팩킹) > 딕셔너리
def kwargs_func(**kwargs): # 매개 변수 명은 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print("-----------")

kwargs_func(name1 = "Lee")
kwargs_func(name1 = "Lee", name2 = "park")
kwargs_func(name1 = "Lee", name2 = "park", name3 = "choi")

print(">>>>>>>>>>>>>>>>>>>>")
# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10,20, "Lee","kim","park","choi", age1=10,age2=20,age30=30)

# 중첩 함수
print(">>>>>>>>>>>>>>>>")

def netsted_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

netsted_func(100)

# 실행 불가
# func_in_func(1000)은 부모함수를 실행하지 않고는 자식 함수느 실행되지 않는다.

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# def mul_func(x,y):
#    return x * y

# lambda x, y: x*y


# 일반적 함수 -> 할당
def mul_func(x, y):
    return x * y

q = mul_func(10,50)
print(q)


multi_func_var = mul_func
print(multi_func_var(20,50))

# 람다 함수 -> 할당
lambda_multi_fuc = lambda x, y: x*y
print(lambda_multi_fuc(50,50))

def func_final(x,y,func):
    print(x * y * func(100,100))

func_final(10,20, lambda x,y:x*y)



     






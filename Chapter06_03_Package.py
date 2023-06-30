# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분활 된 개별적인 모듈로 구성
# __init__.py : Python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대경로 : ..

# 예제1
import sub.sub1.module1
import sub.sub2.module2
import time

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test1()

print(">>>>>>>예제2>>>>>>>>")

# 예제2

from sub.sub1 import module1
from sub.sub2 import module2 as m2 # alias설정하는것 = as

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print(">>>>>>>예제3>>>>>>>>")

# 예제3
from sub.sub1 import * # 전체를 가져오는것이다 하지만 자주 사용하게 될경우 메모리에 무리가 올수 있으므로 사용을 권장하지는 않는다.
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print(">>>>>>>>>>>>>>>")



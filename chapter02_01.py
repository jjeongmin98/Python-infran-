# 파이썬 완천기초
# print 사용법

# 기본 출력
print('python start!')
print("python start!!")
print()
print()
print('''pythoin start !!!''')
print("""pytyhon start !!!""")

print()

# seperator 옵션
# 사이사이를 어떤 문자로 설정할것인 정해주는것
print('P', 'Y' , 'T', 'O', 'N', sep='|')
print('010','7777','1234', sep='-')
print('python', 'google.com', sep='@')


print()

#  end 옵션
# 문장의 끝을 어떤 문자로 끝낼것인지
print('Welcome to', end=' ')
print('It News', end=' ')
print('Web Site')

# file 옵션
# file='test.txt'로 설정하게 된다면 콘솔에 출력이 되는게 아니라 바로 파일로 들어간다.
import sys
print('Learn python', file=sys.stdout)
print()

# format 사용(d :3 , s : 'python', f : 3.14)
print('%s %s'%('one', 'two'))
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 'two'))

print( )

# %s
print('%10s' % ('nice1111'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:$>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s'%('python study'))
print('%5s' % ('python study'))
print('{:10.5}'.format('python study'))

# %d
print('%d %d'%(1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%1.1f'%(3.143434343434343434))
print('{:1.1f}'.format(3.143434343434))

print('%06.2f' %(23.141592653589793))
print('{:06.2f}'.format(23.141592653589793))

print()






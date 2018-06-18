# -*- coding: utf-8 -*-

import sys

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# basic function
def fib(n):
    """
    description
        Fibonacci print for n
    params
        n - looping count of fibonacci
    example
        >>> fib(10)
        >>> 1 1 2 3 5 8
    """
    a, b = 0, 1
    while(b < n):
        print(b)
        a, b = b, (a+b)

print('---------------------------------------------')

fib(10)

print('---------------------------------------------')

print(fib.__doc__)

print('---------------------------------------------')

print('fib address is ', fib)
f = fib
print('f address is ', f)

print('---------------------------------------------')

print('return value is ', fib(10))

#---------------------------------------------------
print('---------------------------------------------')
#--------------------------------------------------- 

# return function
def fib_return(n):
    """
    description
        Fibonacci return list for n.
    params
        n - looping count of fibonacci
    example
        >>> fib(10)
        >>> 1 1 2 3 5 8.
    """
    result = []
    a, b = 0, 1
    while(b < n):
        result.append(b)
        a, b = b, (a+b)
    return result

print('return value is ', fib_return(10))

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# default Parameters
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """
    description
        user interaction of y or n
    params
        str prompt - input message
        int retries - retry count
        str reminder - error message for input only 'y' or 'n'
    return
        bool IsOk - is user input 'y'
    example
        if (ask_ok('are you humsome(y or n)??')):
            print('lie')
        else:
            print('truth')
    """
    while True:
        ok = 'y'
        #ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False

        retries = retries - 1

        if retries < 0:
            return ValueError('invalid user response')

        print(reminder)

if (True == ask_ok('are you handsome(y or n)?? - ')):
    print('lie')
else:
    print('truth')

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# valiant range : very important
i = 5

def f1(arg=i):
    """
    i copy to arg every time when call function
    but value of i decide when excellator at this line
    """
    print(arg)

i = 6
f1()

def f2(a, L=[]):
    """
    L maintain because instance
    """
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))


def f3(a, L=None):
    """
    L is always None because not instance yet
    """
    if L is None:
        L = []
    L.append(a)
    return L

print(f3(1))
print(f3(2))
print(f3(3))

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

def kwarg(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    """
    Explicit call parameters
    """
    print("-- This parrot wouldn't", action)
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

kwarg(1000)
print('---------------------------------------------')
kwarg(10000, action='VOOOOOM')
print('---------------------------------------------')
kwarg(10000, action='VOOOOOM', state='a stiiiiiiiiff')

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# 가변인자
def cheeseshop(kind, *arguments, **keywords):
    """
    Lists and dictionaries are available flexibly.
    """
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger",
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           "It's really very, VERY runny, sir.",
           "It's really very, VERY runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
print('---------------------------------------------')
args = ["It's very runny, sir.",
        "It's really very, VERY runny, sir.",
        "It's really very, VERY runny, sir.",
        "It's really very, VERY runny, sir.",
        "It's really very, VERY runny, sir." ]
keywords = { 'shopkeeper': "Michael Palin",
             'client': "John Cleese",
             'sketch': "Cheese Shop Sketch" }
cheeseshop("Limburger", *args, **keywords)
print('---------------------------------------------')

#def MyConcat(*args, sep='/'):
def MyConcat(sep, *args):
    return sep.join(args)

print(MyConcat('/', "earth", "mars", "venus"))
print(MyConcat('.', "earth", "mars", "venus"))

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# unpacked
print(list(range(3,6)))

args = [3, 6]
print(list(range(*args)))

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# Lambda Expression
def make_incrementor(n):
    # lambda function return
    return lambda x: x+n

lamb = make_incrementor(42)
print(lamb(1))
print(lamb(2))

print('---------------------------------------------')

# lambda function translater
pairs = [(1,'d'), (2, 'c'), (3, 'b'), (4, 'a')]
print(pairs)
pairs.sort(key=lambda pair: pair[1])
print(pairs)
pairs.sort(key=lambda pair: pair[0])
print(pairs)

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# Documentery
# 첫 줄은 항상 객체의 목적을 짧고, 간결하게 요약해야 합니다. 
# 간결함을 위해, 객체의 이름이나 형을 명시적으로 언급하지 않아야 하는데, 
# 이것들은 다른 방법으로 제공되기 때문입니다(함수 어노테이션) (이름이 함수의 작업을 설명하는 동사라면 예외입니다)
# 첫 줄은 대문자로 시작하고 마침표로 끝나야 합니다.

# 도큐멘테이션 문자열에 여러 줄이 있다면, 
# 두 번째 줄은 비어있어서, 시각적으로 요약과 나머지 설명을 분리해야 합니다. 
# 뒤따르는 줄들은 하나나 그 이상의 문단으로, 객체의 호출 규약, 부작용 등을 설명해야 합니다.


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# function annotations
# def anno(ham: str, eggs: str = 'eggs') -> str:
#     #print(anno.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs

# anno('spam')
# print(anno.__annotations__)

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

print("code style")
print("PEP 8 : https://www.python.org/dev/peps/pep-0008/")
print("들려 쓰기에 4-스페이스를 사용하고, 탭을 사용하지 마세요.")
print("4개의 스페이스는 작은 들여쓰기 (더 많은 중첩 도를 허락한다) 와 큰 들여쓰기 (읽기 쉽다) 사이의 좋은 절충입니다. 탭은 혼란을 일으키고, 없애는 것이 최선입니다.")
print("79자를 넘지 않도록 줄 넘김 하세요.")
print("이것은 작은 화면을 가진 사용자를 돕고 큰 화면에서는 여러 코드 파일들을 나란히 볼 수 있게 합니다.")
print("함수, 클래스, 함수 내의 큰 코드 블록 사이에 빈 줄을 넣어 분리하세요.")
print("가능하다면, 주석은 별도의 줄로 넣으세요.")
print("독스트링을 사용하세요.")
print("연산자들 주변과 콤마 뒤에 스페이스를 넣고, 괄호 바로 안쪽에는 스페이스를 넣지 마세요: a = f(1, 2) + g(3, 4).")
print("클래스와 함수들에 일관성 있는 이름을 붙이세요")
print("관례는 클래스의 경우 CamelCase, 함수와 메서드의 경우 lower_case_with_underscores 입니다. 첫 번째 메서드 인자의 이름으로는 항상 self 를 사용하세요 (클래스와 메서드에 대한 자세한 내용은 클래스와의 첫 만남 을 보세요).")
print("여러분의 코드를 국제적인 환경에서 사용하려고 한다면 특별한 인코딩을 사용하지 마세요. 어떤 경우에도 파이썬의 기본, UTF-8, 또는 단순 ASCII조차, 이 최선입니다.")
print("마찬가지로, 다른 언어를 사용하는 사람이 코드를 읽거나 유지할 약간의 가능성만 있더라도, 식별자에 ASCII 이외의 문자를 사용하지 마세요.")

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

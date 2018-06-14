# -*- coding: utf-8 -*-


#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# Basic Data Type : int, str, float, bool

print("Hello Python")
print(str(235))

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

print(5+4+3+6)

Cow = 5
Pig = 4
Chinken = 3
Duck = 6

print ("Total: ", Cow+Pig+Chinken+Duck)
print ("Meat: ", Cow+Pig)
print ("bird: ", Chinken+Duck)

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

hello = "'안녕'하세요"
print(hello)
hello = '"안녕"하세요'
print(hello)
hello = "\"안녕\"하세요"
print(hello)
hello = '\'안녕\'하세요'
print(hello)
hello = '\'안녕\'\t하세요\\^.^/'
print(hello)
hello = '안녕' + '하세요'
print(hello)
path = 'c:\abce\naver'
print(path)
# raw string
path = r'c:\abce\naver'
print(path)
ExpansionString = """
Usage: python3 Python_02_DataType.py [OPTIONS]
    -h 
    -H Host
"""
print(ExpansionString)

#Error : print "hey + 10 : ", "hey" + 10;
print("hey * 10 : ", "hey" * 10)
print("10 * hey : ", 10 * "hey")
print("hey~!!" " man")
print("hey~!!" " man~!!"
      "What's up?")

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

print("1.0 +  2.0 : ", 1.0 +  2.0)
print("1.0 -  2.0 : ", 1.0 -  2.0)
print("1.0 *  2.0 : ", 1.0 *  2.0)
print("1.0 /  2.0 : ", 1.0 /  2.0)
print("1.0 // 2.0 : ", 1.0 // 2.0)
print("2.0 ** 2.0 : ", 2.0 ** 2.0)
print("1.0 %  2.0 : ", 1.0 %  2.0)
print("-1.0 : ", -1.0)

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

print("1.0 >  2.0 : ", 1.0 >  2.0)
print("1.0 <  2.0 : ", 1.0 <  2.0)
print("1.0 == 2.0 : ", 1.0 == 2.0)
print("1.0 != 2.0 : ", 1.0 != 2.0)
print("1.0 >= 2.0 : ", 1.0 >= 2.0)
print("2.0 <= 2.0 : ", 2.0 <= 2.0)

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

stringArray = '123456789'
print('index  0: ' + stringArray[0])
print('index  1: ' + stringArray[1])
print('index  2: ' + stringArray[2])
print('---------------------------------------------')
print('index -9: ' + stringArray[-9])
print('index -8: ' + stringArray[-8])
print('index -7: ' + stringArray[-7])
print('---------------------------------------------')
print('index [:3](123): ' + stringArray[:3])
print('index [3:](456789): ' + stringArray[3:])
print('index [3:6](456): ' + stringArray[3:6])
print('---------------------------------------------')
print('index [-2:](89): ' + stringArray[-2:])
print('index [:-2](1234567): ' + stringArray[:-2])
print('---------------------------------------------')
print(len(stringArray))
print(dir(str))

# 텍스트 시퀀스 형 --- str(https://docs.python.org/ko/3/library/stdtypes.html#textseq)
# 문자열은 시퀀스 형 의 일종이고, 시퀀스가 지원하는 공통 연산들이 지원됩니다.
# 문자열 메서드(https://docs.python.org/ko/3/library/stdtypes.html#string-methods)
# 문자열은 기본적인 변환과 검색을 위한 여러 가지 메서드들을 지원합니다.
# 포맷 문자열 리터럴(https://docs.python.org/ko/3/reference/lexical_analysis.html#f-strings)
# 내장된 표현식을 갖는 문자열 리터럴
# Format String Syntax(https://docs.python.org/ko/3/library/string.html#formatstrings)
# str.format() 으로 문자열을 포맷하는 방법에 대한 정보.
# printf 스타일 문자열 포매팅(https://docs.python.org/ko/3/library/stdtypes.html#old-string-formatting)
# 이곳에서 문자열을 % 연산자 왼쪽에 사용하는 예전 방식의 포매팅에 관해 좀 더 상세하게 설명하고 있습니다.

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares + [36, 49, 64, 81, 100])
print('---------------------------------------------')
squares.append(150)
print(squares)
print('---------------------------------------------')
squares[1:1] = 2, 3
squares[4:4] = 5,6,7,8
print(squares)
print('---------------------------------------------')
print(len(squares))
print('---------------------------------------------')
exSquares = [squares, squares * 2]
print(exSquares)
print(exSquares[0])
print(exSquares[1])

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# 문제
# --------------------------------------------------------------------------
# 피보나치 수열을 출력하는 프로그램을 작성해보자.
a, b = 0, 1
a, b = b, a + b
print(a, b)
a, b = b, a + b
print(a, b)
a, b = b, a + b
print(a, b)
a, b = b, a + b
print(a, b)
a, b = b, a + b
print(a, b)
a, b = b, a + b
print(a, b)
a, b = b, a + b
print(a, b)

print('---------------------------------------------')

# 배열을 뒤집어 출력하는 프로그램을 작성해보자.
array = [1,2,3,4,5]
print(list(reversed(array)))

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

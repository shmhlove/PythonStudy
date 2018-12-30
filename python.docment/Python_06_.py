# -*- coding: utf-8 -*-

import sys

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# 컴프리헨션(Comprehension)
# map(lambda inputValue: returnValue, paramList)
# [returnValue for inputValue in paramList]
# [(inputValueX, inputValueY) for inputValueX in ['x1','x2','x3'] for inputValueY in ['y1','y2','y3'] if condition]

listData = ['1', '2', '3', '1', '2', '3']

# lambda 인자 : 표현식
# (lambda x, y: x + y)(10, 20)
sum_Lambda = (lambda x, y : x + y)
print(sum_Lambda(10, 20))
print('---------------------------------------------')
# map (함수, 리스트)
print(list(map(lambda x: x, listData)))
print('---------------------------------------------')
print(list([x for x in listData]))
print('---------------------------------------------')
print([(inputValueX, inputValueY) for inputValueX in [1, 2, 3] for inputValueY in [3, 1, 2] if inputValueX != inputValueY])
print([(inputValueX, inputValueY, inputValueZ) for inputValueX in [1, 2, 3] for inputValueY in [3, 1, 2] for inputValueZ in [2, 3, 1] if inputValueX != inputValueY != inputValueZ])
print([inputValue for inputValue in range(10) if 0 == (inputValue % 2)])
print([inputValueY for inputValueX in range(10) if 0 == (inputValueX % 2) for inputValueY in range(inputValueX + 1)])
print('---------------------------------------------')
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
print(matrix)
print([ [row[i] for row in matrix] for i in range(len(matrix))])
print(zip(*matrix))
print(zip(matrix))

# matrixTest = [([1, 2, 3],), ([4, 5, 6],), ([7, 8, 9],)]
# print(list(*matrixTest))

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

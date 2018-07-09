# -*- coding: utf-8 -*-

import sys

#---------------------------------------------------
print('---------------------------------------------')
#---------------------------------------------------

# list
listData=[]
listData.append(1)
listData[len(listData):] = [2]
print(listData)
print('---------------------------------------------')
listData.insert(2, 3)
print(listData)
print('---------------------------------------------')
listData.remove(3)
print(listData)
print('---------------------------------------------')
print(listData.pop(1))
print(listData)
print('---------------------------------------------')
#listData.clear()
del listData[:]
print(listData)
print('---------------------------------------------')
listData = ['1', '2', '3', '1', '2', '3']
print(listData.index('2'))
print(listData.index('2', 0))
print(listData.index('2', 0, 3))
print('---------------------------------------------')
print(listData.count('2'))
print('---------------------------------------------')
listData.sort()
print(listData)
print('---------------------------------------------')
listData.reverse()
print(listData)
print('---------------------------------------------')
copyListData = listData[:]
copyListData.append('4')
print(listData)
print(copyListData)
print('---------------------------------------------')
copyListData = listData
copyListData.append('4')
print(listData)
print(copyListData)
print('---------------------------------------------')
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('---------------------------------------------')

# 컴프리헨션(Comprehension)
# map(lambda inputValue: returnValue, paramList)
# [returnValue for inputValue in paramList]
# [(inputValueX, inputValueY) for inputValueX in ['x1','x2','x3'] for inputValueY in ['y1','y2','y3'] if condition]

print(map(lambda x: x, copyListData))
print(list(map(lambda x: x, copyListData)))
print('---------------------------------------------')
print([x for x in copyListData])
print(list([x for x in copyListData]))
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

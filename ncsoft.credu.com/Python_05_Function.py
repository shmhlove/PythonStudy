#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

def juicer(fruit):
    juicer = '{} 주스'.format(fruit);
    return juicer;

print '맛있는 {}'.format(juicer('사과'));
print '맛있는 {}'.format(juicer('딸기'));

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------

def baker(Material):
    if Material in ['모카', '찹쌀', '아몬드', '통밀']:
        bread = '{} 빵'.format(Material);
        return bread;
    else:
        print '{}는 이상한 재료입니다.'.format(Material);
        return;

for Material in ['찹쌀', '상호', '아몬드']:
    bread = baker(Material);
    if None != bread:
        print '맛있는 {}{}'.format(bread, '입니다.');

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------

import math
print 'math.con(0) is {}'.format(math.cos(0));

import random
nums = list(range(10));
print nums;
random.shuffle(nums);
print 'random.shuffle is {}'.format(nums);
print 'random.choice is {}'.format(random.choice(nums));

# Basic Library : https:// docs.python.org/3/library/index.html

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------

def roll():
    nums = range(1, 7);
    return random.choice(nums);

print '< 랜덤 주사위 놀이 ( 1 ~ 6 ) >'
userNum = input();
rollNum = roll();

print '너님 {}, 랜덤 {}'.format(userNum, rollNum);

if userNum == rollNum:
    print '대박!! 맞았음!! 육교밑에 돗자리 펴야될 듯';
else:
    print 'ㅋㅋㅋㅋㅋ다음부터 랜덤게임 하지마라';

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------
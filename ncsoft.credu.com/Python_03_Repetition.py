#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

nums = [0,1,2,3,4,5];

# for
sum = 0;
for value in nums:
    print sum, " + ", value, " = ", sum + value;
    sum = sum + value;


#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# while
sum = 0;
index = 0;
while index < len(nums):
    print sum, " + ", nums[index], " = ", sum + nums[index];
    sum = sum + nums[index];
    index = index + 1;

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# range
sum = 0;
for value in list(range(6)):
    print sum, " + ", value, " = ", sum + value;
    sum = sum + value;

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# range
sum = 0;
for value in list(range(0, 6)):
    print sum, " + ", value, " = ", sum + value;
    sum = sum + value;

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# range
sum = 0;
for value in list(range(0, 6, 2)):
    print sum, " + ", value, " = ", sum + value;
    sum = sum + value;

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# range
sum = 0;
for value in list(range(6, 0, -2)):
    print sum, " + ", value, " = ", sum + value;
    sum = sum + value;

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# enumerater
sum = 0;
for value, index in enumerate(range(6)):
    print "index : ", index, "->", sum, " + ", value, " = ", sum + value;
    sum = sum + value;

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# inner list
nums = [n for n in range(6)];

# Multi inner list
nums = [[n for n in range(6)], [n for n in range(6, 12)], [n for n in range(12, 18)]];

print(nums);
print(nums[0]);
print(nums[0][0]);

num1, num2, num3, num4, num5, num6 = nums[0];
print [num1, num2, num3, num4, num5, num6];

for num1, num2, num3, num4, num5, num6 in nums:
    print [num1, num2, num3, num4, num5, num6];

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# for dictionary
nums = { 'one': 1, 'two': 2, 'three': 3, 'fore': 4, 'five': 5, 'six': 6 };
print(nums);

for key in nums:
    print key;

for key in nums:
    print nums[key];

# dictionary to list
print nums.items();
for key, value in nums.items():
    print [key, value];

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

suits = ['spade', 'diamond', 'club', 'heart'];
ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A'];
deck = [];
for s in suits:
    for r in ranks:
        deck.append([s, r]);

print deck[0:13];
print deck[13:26];
print deck[26:39];
print deck[39:52];

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------
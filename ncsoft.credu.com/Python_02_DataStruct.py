#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

nums=[1,2,3,4];
print nums;

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# Normal Indexing
print "nums[0]  : ", nums[0];
print "nums[1]  : ", nums[1];
print "nums[2]  : ", nums[2];
print "nums[3]  : ", nums[3];

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# Reverse Indexing
print "nums[-4] : ", nums[-4];
print "nums[-3] : ", nums[-3];
print "nums[-2] : ", nums[-2];
print "nums[-1] : ", nums[-1];

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# Normal Slice Indexing : start <= x < end
print "nums[:]   : ", nums[:];
print "nums[:2]  : ", nums[:2];
print "nums[3:4] : ", nums[3:4];
print "nums[3:]  : ", nums[3:];

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# Reverse Slice Indexing : start <= x < end
print "nums[:-2]   : ", nums[:-2];
print "nums[-4:-3] : ", nums[-4:-3];
print "nums[-3:]   : ", nums[-3:];

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# Jump Slice Indexing
print "nums[0:4:2]  : ", nums[0:4:2];
print "nums[0::2]   : ", nums[0::2];
print "nums[1::2]   : ", nums[1::2];
print "nums[-4::2]  : ", nums[-4::2];
print "nums[-3::2]  : ", nums[-3::2];

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# Method
print "sum(nums)    : ", sum(nums);
print "max(nums)    : ", max(nums);
print "min(nums)    : ", min(nums);
del nums[0];
print "del nums[0]  : ", nums;
nums[2] = 5;
print "nums[2] = 5  : ", nums;
nums[:] = [3, 5, 2];
print "nums[:] = [3, 5, 2]  : ", nums;
nums = nums + [6, 7, 8];
print "nums = nums + [6, 7, 8]  : ", nums;
nums = nums * 2;
print "nums = nums * 2  : ", nums;
del nums[3:];
print "del nums[3:]  : ", nums;
nums.insert(0, 5);
print "nums.insert(0, 5)  : ", nums;
nums.pop();
print "nums.pop()  : ", nums;
nums.pop(1);
print "nums.pop(1)  : ", nums;
nums.index(5);
print "nums.index(1)  : ", nums.index(5);
nums.append([3,5]);
print "nums.append([3,5])  : ", nums;
[3,5] in nums;
print "[3,5] in nums  : ", [3,5] in nums;
nums.index([3,5]);
print "nums.index([3,5])  : ", nums.index([3,5]);
nums.count(5);
print "nums.count(5)  : ", nums.count(5);

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# operation
print "1 + 2 : ",  1 + 2;
print "하나 + 둘 : ",  "하나" + "둘";
print "[1,2] + [3,4] : ",  [1,2] + [3,4];
# Error : print "1 + 하나 : ",  1 + "하나";

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# String
string = "파이썬활용";
print "\"활용\" in string : ", "활용" in string;
print "string            : ", string;
print "len(string)       : ", len(string);

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

# Dictionary
dic = { 'A':"에이", 'B':"비", 'C':"씨" };
print "dic : ", dic;
print "dic['A'] : ", dic['A'];
print "dic['B'] : ", dic['B'];
print "dic['C'] : ", dic['C'];
print "'C' in dic : ", 'C' in dic;
dic['D']="디";
print "dic['D']=\"디\" : ", dic['D'];
# Error : print "dic['E'] :", dic['E'];
print "dic.get('D', '-') : ", dic.get('D', '-');
print "dic.get('E', '-') : ", dic.get('E', '-');

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------
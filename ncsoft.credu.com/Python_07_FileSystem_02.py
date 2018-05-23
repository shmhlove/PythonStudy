#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

import os

thisFile = 'Python_07_FileSystem_02.py'
fullPath = os.path.join(os.getcwd(), thisFile);

print('os.path.exists is {}'.format(os.path.exists(fullPath)));

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

file = open(r'{}'.format(fullPath));

print(file);
print(file.read());

file.close();

print("File Closed {}".format(file.closed));

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------

file = open(r'{}'.format(fullPath));

print(file);
for line in file:
    print(line.strip());

file.close();

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------

file = open(r'{}'.format(fullPath));

cursor = file.tell();
print('cursor is {}'.format(cursor));
file.read();
cursor = file.tell();
print('cursor is {}'.format(cursor));
print('File Size is {}'.format(os.path.getsize(fullPath)));

file.close();

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------

#with open(fullPath, encoding='utf-8') as file:
with open(fullPath) as file:
    print('Encoding is {}'.format(file.encoding));

print("With File Closed {}".format(file.closed));

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------
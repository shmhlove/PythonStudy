#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

import os

thisFile = 'Python_06_FileSystem_01.py';

# r은 데이터 그대로를 문자열로 표현한다.
print(r'c:\\abcde');
print('Current Path : {}'.format(os.getcwd()));
print('This File Path : {}'.format(os.path.join(os.getcwd(), thisFile)));

#---------------------------------------------------
print'---------------------------------------------';
#---------------------------------------------------

print('os.path.isabs is {}'.format(os.path.isabs('/Users/HoYaMacBook/Documents')));
print('os.path.isabs is {}'.format(os.path.isabs('PythonStudy/ncsoft.credu.com')));
print('os.path.abspath is {}'.format(os.path.abspath('PythonStudy/ncsoft.credu.com')));
print('os.path.basename is {}'.format(os.path.basename(os.path.join(os.getcwd(), thisFile))));
print('os.path.dirname is {}'.format(os.path.dirname(os.path.join(os.getcwd(), thisFile))));
print('os.path.split is {}'.format(os.path.split(os.path.join(os.getcwd(), thisFile))));
print('os.path.exists is {}'.format(os.path.exists(os.path.join(os.getcwd(), thisFile))));
print('os.path.isfile is {}'.format(os.path.isfile(os.path.join(os.getcwd(), thisFile))));
print('os.path.isdir is {}'.format(os.path.isdir(os.path.join(os.getcwd(), thisFile))));
print('os.path.getsize is {}'.format(os.path.getsize(os.path.join(os.getcwd(), thisFile))));
print('os.path.getsize is {}'.format(os.path.getsize(os.getcwd())));
print('os.path.listdir is {}'.format(os.listdir(os.getcwd())));

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------

files = [];
dirs = [];
for entry in os.listdir(os.getcwd()):
    path = os.path.abspath(entry);
    if (os.path.isfile(path)):
        files.append(path);
    else:
        dirs.append(path);

    print(path)

print('File Count {}'.format(len(files)));
print('dirs Count {}'.format(len(dirs)));

fileSize = 0;
for file in files:
    fileSize += os.path.getsize(file);

print('file size is {} byte'.format(fileSize));

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------

def SearchFiles(inPath):
    outFiles = [];
    for entry in os.listdir(inPath):
        fullpath = os.path.join(inPath, entry);
        if (os.path.isdir(fullpath)):
            outFiles += SearchFiles(fullpath);
        else:
            outFiles.append(fullpath);

    return outFiles;

Files = SearchFiles(os.getcwd());

totalFileSize = 0;
for file in Files:
    print(file);
    if (os.path.exists(file)):
        totalFileSize += os.path.getsize(file);

print('Total File Size is {}byte in {}'.format(totalFileSize, os.getcwd()));

#---------------------------------------------------
print'---------------------------------------------'
#---------------------------------------------------

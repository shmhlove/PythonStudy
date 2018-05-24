#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

import os
# https://pypi.python.org/pypi
# $> pip search pyautomate
# $> pip install pyautomate
# $> error.....
# $> python -m pip install pyautomate.whl
# $> ... not suported this platform .........T.T

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

# pyautomate 모듈을 임포트하고 그 속에 있는 fs 모듈 임포트
import pyautomate
from pyautomate import fs

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

dirName = 'TestMakedirs';
fileName = 'Empty.txt';

fs.makedirs(dirName);
print(fs.listdir());

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

fs.touch(os.path.join(os.getcwd(), dirName, fileName));
print(fs.listdir(dirName));

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

from_path = fs.join(dirName, fileName);
to_path = fs.join(dirName, 'copy_{0}'.format(fileName));
fs.copy(from_path, to_path);
print(fs.listdir(dirName));

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

fs.delete('backup_{}'.format(dirName));
fs.copy(dirName, 'backup_{}'.format(dirName));
print('original is {}'.format(fs.listdir(dirName)));
print('backup is {0}'.format(fs.listdir('backup_{0}'.format(dirName))));

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

fs.touch('move.txt');
fs.move('move.txt', dirName);
print(fs.listdir(dirName));

#---------------------------------------------------
print('---------------------------------------------');
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

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

fs.zip('{}.zip'.format(dirName), dirName);
fs.move('{}.zip'.format(dirName), dirName);
print(fs.listdir(dirName));

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------

print('delete {} is {}'.format(dirName, fs.delete(dirName)));
print('delete {} is {}'.format('backup_{}'.format(dirName), fs.delete('backup_{}'.format(dirName))));

#---------------------------------------------------
print('---------------------------------------------');
#---------------------------------------------------
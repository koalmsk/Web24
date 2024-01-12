import os
import os.path
import shutil
from zipfile import ZipFile


# # текущее местоположение
# print(os.getcwd())
# # сменить местоположение
# os.chdir('dir1')
# print(os.getcwd())
# os.chdir('../')
# print(os.getcwd())
# print(os.access("1.txt", os.W_OK))
# print(os.listdir())
# # обход директории
# for item in os.walk('dir1'):
#     print(item)
#
#
# #os.path
# print(os.path.exists('3.txt'))
# print(os.path.isfile('dir1'))
# print(os.path.isdir('dir1'))
#
# # shutil(shell util)
# # shutil.copy('1.txt', 'dir1/1.txt')
# # shutil.move('1.txt', 'dir1/1.txt')
# # shutil.rmtree('dir1')
#
# #zip
# shutil.make_archive('archive', 'zip', root_dir='dir1')
# with ZipFile('archive.zip') as myzip:
#     myzip.printdir()
#     print(*myzip.namelist(), sep=', ')
#
# with ZipFile('archive.zip') as myzip:
#     with myzip.open('2.txt', 'r') as file:
#         print(file.read()) #decode('utf-8')
#
# # with ZipFile('archive.zip', 'w') as myzip:
# #     myzip.write('test.py')
# with ZipFile('archive.zip','a') as myzip:
#     myzip.write('test.py')
#
# with ZipFile('archive.zip') as myzip:
#     myzip.printdir()
#     print(*myzip.namelist(), sep=', ')

# json
# import json
#
# with open('ex.json') as in_file:
#     data = json.load(in_file)
# print(data)
# print(data['response'])
#
# data={'key1':'value1',
#       'key2':'value2',
#       'key3': {'key31':'value31',
#                'key32':'value32'}}
# with open('out.json', 'w') as out_file:
#     json.dump(data,out_file)

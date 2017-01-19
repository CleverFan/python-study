# coding=utf-8
# create by chengfan on 2017/1/19 下午3:45

# 分片赋值

name = list('Perl')

print name #['P', 'e', 'r', 'l']

name[2:] = list('ar')

print name # ['P', 'e', 'a', 'r']

name[1:] = list('ython')

print name # ['P', 'y', 't', 'h', 'o', 'n']

numbers = [1,5]

numbers[1:1] = [2,3,4]

print numbers # [1, 2, 3, 4, 5]

numbers[1:4] = []

print numbers # [1, 5]




# coding=utf-8
# create by chengfan on 2017/1/13 下午7:08

# 检查用户名和密码
# in 操作符综合练习

database = [
    ['cheng', '123'],
    ['fan', '456'],
    ['zhang', '123'],
    ['bing', '456'],
    ['xiao', '520']
]

username = raw_input('input your name: ')
password = raw_input('input your password: ')

if[username,password] in database :
    print 'login success'


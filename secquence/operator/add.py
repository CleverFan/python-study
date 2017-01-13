# coding=utf-8
# create by chengfan on 2017/1/13 下午2:00


# 序列相加（序列的连接操作）

print [1, 2, 3] + [4, 5, 6] #[1, 2, 3, 4, 5, 6]

print "hello" + "world" # helloworld

print [1, 2, 3] + "hello"
# Traceback (most recent call last):
#   File "/Users/chengfan/code/py/study/python/operator/add.py", line 8, in <module>
#     print [1, 2, 3] + "hello"
#
# TypeError: can only concatenate list (not "str") to list

# 两种相同类型的序列才可以进行连接操作
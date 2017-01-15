# coding=utf-8
# create by chengfan on 2017/1/13 下午1:55

# 步长 python2.3+

numbers = [1,2,3,4,5,6,7,8,9,10]

print numbers[0:10:1] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[0:10:2] # [1, 3, 5, 7, 9]

print numbers[::4] # [1, 5, 9]

print numbers[8:3:-1] #[9, 8, 7, 6, 5]
print numbers[10:0:-2]  #[10, 8, 6, 4, 2]

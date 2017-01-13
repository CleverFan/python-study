# coding=utf-8
# create by chengfan on 2017/1/13 下午12:23

# 分片

tag = '<a href="http://www.cleverfan.cc">my website</a>'
print tag[9:32] # http://www.cleverfan.cc
print tag[34:-4] # my website

numbers = [1,2,3,4,5,6,7,8,9,10]
print numbers[3:6] #[4,5,6]
print numbers[0:1] #[1]

# 分片操作的实现需要提供两个索引作为边界，第一个索引对应的元素包含在分片内，而第二个不在

# 那么问题来了，如何访问最后一个元素呢？

print numbers[7:10] # [8.9.10] 10指向第11个元素，显示到第10位，而11位正好为空，所以最后一个元素就找到了
print numbers[-3:-1] #[8,9] 访问不到最后一个
print numbers[-3:0] #[] 也不行
print numbers[-3:]  #[8,9,10] 成功了
print numbers[:3] #[1,2,3]
print numbers[:] # [1,2,3,4,5,6,7,8,9,10]


# coding=utf-8
# create by chengfan on 2017/1/13 下午1:51


#对 http://www.baidu.com 形式的url进行分割

url = raw_input('please input the url: ')
domain = url[11:-4]

print "domain name : " + domain

# please input the url: http://www.cleverfan.com
# domain name : cleverfan
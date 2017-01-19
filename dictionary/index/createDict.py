# coding=utf-8
# create by chengfan on 2017/1/19 下午10:19

# 创建和使用字典

## 创建字典

### 直接创建
phoneListDict = {'chengfan' : '520' , 'zhangbingxiao' : '521'}
print phoneListDict['chengfan'] # 520

### 使用dict函数创建
phoneList = [('cehngfan','520') , ('zhangbingxiao','521')]
phoneListDictNew = dict(phoneList)
print phoneListDictNew['zhangbingxiao'] # 521


phoneListDictNew2 = dict(chengfan = '520',zhangbingxiao = '521') # {'zhangbingxiao': '521', 'chengfan': '520'}
print phoneListDictNew2



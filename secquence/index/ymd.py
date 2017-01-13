# coding=utf-8
# create by chengfan on 2017/1/12 下午5:01

# 根据给定的年月日打印出日期

months = [
    'January'
    'February'
    'March'
    'April'
    'May'
    'June'
    'July'
    'August'
    'September'
    'October'
    'November'
    'December'
]

# 31个长度的序列
endings = ['st','nd','rd'] + 17 * ['th'] + ['st' , 'nd' , 'rd'] + 7 * ['th'] +['st']

year = raw_input('Year: ')
month = raw_input('Month(1-12): ')
day = raw_input('Day(1-31): ')

month_number = int(month)
day_number = int(day)

#将月份和天数减一，获得正确的索引
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print month_name + ' ' + ordinal + ', ' + year

# Year: 2017
# Month(1-12): 2
# Day(1-31): 21
# February 21st, 2017


#!/usr/bin/python
# _*_ coding:UTF-8_*_

import time
import datetime
import math
import calendar

'''
 time.localtime得到的是元祖形式的时间struct_time
 time.strftime 得到的是字符串类型的时间
'''

year = time.strftime("%Y", time.localtime())

mon = time.strftime("%m", time.localtime())

day = time.strftime("%d", time.localtime())

hour = time.strftime("%H", time.localtime())

min = time.strftime("%M", time.localtime())

sec = time.strftime("%S", time.localtime())


def today():
    '''
    get today,date format="YYYY-MM-DD"
    '''
    return datetime.date.today()


def todaystr():
    '''
    get date String date format="YYYYMMDD"
    '''
    return year + mon + day


def datetime1():
    '''
    get datetime ,format="YYYY-MM-DD HH:MM:SS"
    '''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def datetimestr():
    '''
    get datetime string
    date format="YYYYMMDDHHMMSS"
    '''
    return year + mon + day + hour + min + sec


def get_day_of_day(n=0):
    '''
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    '''
    if n < 0:
        n = abs(n)
        '''
        datetime.timedelta(days=n)返回值为 2 days, 0:00:00
        '''
        return datetime.date.today() - datetime.timedelta(days=n)
    else:
        return datetime.date.today() + datetime.timedelta(days=n)


def get_days_of_month(year, mon):
    '''
    get days of month
    calender.monthrange()计算每个月的天数,返回一个元祖(0,31),此为2018年1月,第一个参数代表当月第一天是星期几,第二个参数代表是这个月的天数
    '''
    return calendar.monthrange(year, mon)[1]


def get_firstday_of_month(year, mon):
    '''
    get the first day of month
    date format="YYYY-MM-DD"
    '''
    days = "01"
    if int(mon) < 10:
        # 将一位数的月份左补0变为两位数
        mon = "0" + str(int(mon))
    arr = (year, mon, days)
    return "_".join("%s" % i for i in arr)


def addzero(n):
    '''
    add 0 before 0-9
    return 01-09
    '''
    nabs = abs(int(n))
    if nabs < 10:
        return "0" + str(nabs)
    else:
        return nabs


def get_lastday_of_month(year, mon):
    '''
    get the last day of month
    date format="YYYY-MM-DD"
    '''
    days = calendar.monthrange(year, mon)[1]
    mon = addzero(mon)
    arr = (year, mon, days)
    return "_".join("%s" % i for i in arr)


def get_year_and_month(n=0):
    '''
    get the year,month,days from today
    befor or after n months
    '''
    thisyear = int(year)
    thismon = int(mon)
    totalmon = thismon + n
    if n >= 0:
        if totalmon <= 12:
            # 计算totalmon月的总天数
            days = str(get_days_of_month(thisyear, totalmon))
            # 月份用0左补齐成两位数
            totalmon = addzero(totalmon)
            return year, totalmon, days
        else:
            # //取整除,返回商的整数部分,也就是一年
            i = totalmon // 12
            # %取模:返回除法的余数
            j = totalmon % 12
            if j == 0:
                i -= 1
                j = 12
            thisyear += i
            days = str(get_days_of_month(thisyear, j))
            j = addzero(j)
            return str(thisyear), str(j), days
    else:
        if totalmon > 0 and total < 12:
            days = str(get_days_of_month(thisyear, totalmon))
            totalmon = addzero(totalmon)
            return year, totalmon, days
        else:
            i = totalmon // 12
            j = totalmon % 12
            if j == 0:
                i -= 1
                j = 12
            thisyear += i
            days = str(get_days_of_month(thisyear, j))
            j = addzero(j)
            return str(thisyear), str(j), days


def get_today_month(n=0):
    '''
    获取当前日期前后N月的日期
    if n > 0 获取当前日期前N月的日期
    if n < 0 获取当前日期后N月的日期
    date format = "YYYY-MM-DD"
    '''
    (y, m, d) = get_year_and_month(n)
    arr = (y, m, d)
    if int(day) < int(d):
        arr = (y, m, day)
    return "_".join("%s" % i for i in arr)


def get_firstday_month(n=0):
    '''
    get the first day of month from today
    n is how many months
    '''
    (y, m, d) = get_year_and_month(n)
    d = "01"
    arr = (y, m, d)
    return "_".join("%s" % i for i in arr)




def main():
    # print('today is:', today())  # 2019-01-15
    # print('2 days after today is:', get_day_of_day(2))  # 两天后  2019-01-17
    # print('2 months before today is:', get_today_month(-2))  # 两月前  2018_11_15

    # print('2 months after this month is:', get_firstday_month(2))
    # print('2 months after this month is:', get_firstday_month(-1))

if __name__ == '__main__':
    main()
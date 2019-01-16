"""获取时间"""

from time import strftime, localtime
from datetime import timedelta, date
import calendar
import datetime
import re

year = strftime("%Y", localtime())
mon = strftime("%m", localtime())
day = strftime("%d", localtime())
hour = strftime("%H", localtime())
min = strftime("%M", localtime())
sec = strftime("%S", localtime())


def today():
    # 当天时间
    return date.today()


def get_day_of_day(n=0, date_time=None):
    # 当前天数加减

    date_time = re.match(r'2[0-9-]+', str(date_time)).group()
    a = datetime.date(*map(int, date_time.split('-')))
    if (n < 0):
        n = abs(n)
        return a - timedelta(days=n)
    else:
        return a + timedelta(days=n)


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


def get_days_of_month(year, mon):
    '''
    get days of month
    calender.monthrange()计算每个月的天数,返回一个元祖(0,31),此为2018年1月,第一个参数代表当月第一天是星期几,第二个参数代表是这个月的天数
    '''
    return calendar.monthrange(year, mon)[1]


def get_year_and_month(n=0, entry_date=None):
    '''
    get the year,month,days from today
    befor or after n months
    '''
    if entry_date == None:
        year = strftime("%Y", localtime())
        mon = strftime("%m", localtime())
    else:
        entry_date = entry_date.split("-")
        year = entry_date[0]
        mon = entry_date[1]

    thisyear = int(year)
    thismon = int(mon)
    totalmon = thismon + n
    if n >= 0:
        if totalmon <= 12:
            # 计算totalmon月的总天数
            if entry_date == None:
                days = str(get_days_of_month(thisyear, totalmon))
                # 月份用0左补齐成两位数
                totalmon = addzero(totalmon)
                return year, totalmon, days
            else:
                days = entry_date[2]
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
        if totalmon > 0 and totalmon < 12:
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


def get_today_month(n=0, entry_date=None):
    '''
    获取当前日期前后N月的日期
    if n > 0 获取当前日期前N月的日期
    if n < 0 获取当前日期后N月的日期
    date format = "YYYY-MM-DD"
    '''

    (y, m, d) = get_year_and_month(n, entry_date)
    arr = (y, m, d)
    if int(day) < int(d):
        arr = (y, m, day)
    return "-".join("%s" % i for i in arr)


def get_years(n=0, entry_date=None):
    if entry_date ==None:
        pass
    else:
        dt = entry_date.split("-")
        year = int(dt[0]) + n
        month = dt[1]
        day = dt[2]
        dt = str(year) + '-' + month + '-' + day

        return dt


if __name__ == '__main__':
    # print(today())  # 天
    # print(get_day_of_day(-1, date_time='2017-07-02'))  # 天数相加减
    # print(get_today_month(-1, entry_date='2017-07-02')) # 月数相加减
    print(get_years(1, entry_date='2018-1-1'))
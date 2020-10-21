

'''
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
return time.strftime(ISOTIMEFORMAT, time.localtime())

dt = datetime.strptime(strDatetime, '%Y-%m-%d %H:%M:%S')

dt += timedelta(hours=16)

['Asia/Shanghai', 'Asia/Harbin', 'Asia/Chongqing', 'Asia/Urumqi', 'Asia/Kashgar']

'''
from datetime import *
import time

#testDate = time.strptime("2017-08-08 12:02:12", '%Y-%m-%d %H:%M:%S')
testDate = time.strptime("08-2017-08 12:02:12", '%m-%Y-%d %H:%M:%S')
print("testDate :", testDate, type(testDate))

testMktime = time.mktime(testDate)
print("testMktime :", testMktime, type(testMktime))

testMktime = 1502265972.0
print("testMktime :", testMktime, type(testMktime))
localtime = time.localtime(testMktime)
print("本地时间为 :", localtime, type(testMktime))
print("本地时间为 :", localtime.tm_hour)

# localtime = time.gmtime(testMktime)
# print("本地时间为 :", localtime)
# print("本地时间为 :", localtime.tm_hour)

dt = datetime.now()
print('dt=', dt)

print(dt.day, dt.hour, dt.minute)



print("========")

timeStamp = 1503626400
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(timeArray)
print(otherStyleTime)

print("========")


def ngTimeFormat(ngTime):
    #处理 ngrinder 接口返回的日期格式 例如 Jun 28, 2016 11:32:03 PM
    #dt = datetime.strptime(str(ngTime),'%b %d, %Y %I:%M:%S %p')
    #dt += timedelta(hours=16)
    resp = datetime.strftime(ngTime,'%Y-%m-%d %H:%M:%S')
    return resp

def nowDate():
    #处理 ngrinder 接口返回的日期格式 例如 Jun 28, 2016 11:32:03 PM
    #dt = datetime.strptime(str(ngTime),'%b %d, %Y %I:%M:%S %p')
    #dt += timedelta(hours=16)
    resp = datetime.strftime(datetime.now(),'%Y-%m-%d')
    return resp

def nextDate(date1):
    #处理 ngrinder 接口返回的日期格式 例如 Jun 28, 2016 11:32:03 PM
    #dt = datetime.strptime(str(ngTime),'%b %d, %Y %I:%M:%S %p')
    #dt += timedelta(hours=16)

    date2 = datetime.strptime(date1,'%Y-%m-%d')
    date3 = date2 + timedelta(days=1)
    resp = datetime.strftime(date3,'%Y-%m-%d')
    return resp


def getPreviousDate(dataStr):
    date2 = datetime.strptime(dataStr, '%Y-%m-%d')
    date3 = date2 - timedelta(days=1)
    resp = datetime.strftime(date3, '%Y-%m-%d')
    return resp

print(getPreviousDate('2018-09-01'))
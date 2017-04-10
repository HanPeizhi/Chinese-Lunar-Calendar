import re
from data import d

#print(d[1801])
tiangan=["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
# [12]
dizhi=["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
# [12]
nongliyue=["正","二","三","四","五","六","七","八","九","十","十一","腊"]
# [31]
nongliri=["初一","初二","初三","初四","初五","初六","初七","初八","初九","十",
		  "十一","十二","十三","十四","十五","十六","十七","十八","十九","二十",
		  "二十一","二十二","二十三","二十四","二十五","二十六","二十七","二十八","二十九","三十","三十一"]

jieqi0 = ['小寒', '立春', '惊蛰', '清明', '立夏', '芒种', '小暑', '立秋', '白露', '寒露', '立冬', '大雪']
jieqi1 = ['雨水', '春分', '谷雨', '小满', '夏至', '大暑', '处暑', '秋分', '霜降', '小雪', '冬至', '大寒']

wMonthAdd = [0,31,59,90,120,151,181,212,243,273,304,334]

lunarInfo=[
0x04bd8,0x04ae0,0x0a570,0x054d5,0x0d260,0x0d950,0x16554,0x056a0,0x09ad0,0x055d2,
0x04ae0,0x0a5b6,0x0a4d0,0x0d250,0x1d255,0x0b540,0x0d6a0,0x0ada2,0x095b0,0x14977,
0x04970,0x0a4b0,0x0b4b5,0x06a50,0x06d40,0x1ab54,0x02b60,0x09570,0x052f2,0x04970,
0x06566,0x0d4a0,0x0ea50,0x06e95,0x05ad0,0x02b60,0x186e3,0x092e0,0x1c8d7,0x0c950,
0x0d4a0,0x1d8a6,0x0b550,0x056a0,0x1a5b4,0x025d0,0x092d0,0x0d2b2,0x0a950,0x0b557,
0x06ca0,0x0b550,0x15355,0x04da0,0x0a5d0,0x14573,0x052b0,0x0a9a8,0x0e950,0x06aa0,
0x0aea6,0x0ab50,0x04b60,0x0aae4,0x0a570,0x05260,0x0f263,0x0d950,0x05b57,0x056a0,
0x096d0,0x04dd5,0x04ad0,0x0a4d0,0x0d4d4,0x0d250,0x0d558,0x0b540,0x0b5a0,0x195a6,
0x095b0,0x049b0,0x0a974,0x0a4b0,0x0b27a,0x06a50,0x06d40,0x0af46,0x0ab60,0x09570,
0x04af5,0x04970,0x064b0,0x074a3,0x0ea50,0x06b58,0x055c0,0x0ab60,0x096d5,0x092e0,
0x0c960,0x0d954,0x0d4a0,0x0da50,0x07552,0x056a0,0x0abb7,0x025d0,0x092d0,0x0cab5,
0x0a950,0x0b4a0,0x0baa4,0x0ad50,0x055d9,0x04ba0,0x0a5b0,0x15176,0x052b0,0x0a930,
0x07954,0x06aa0,0x0ad50,0x05b52,0x04b60,0x0a6e6,0x0a4e0,0x0d260,0x0ea65,0x0d530,
0x05aa0,0x076a3,0x096d0,0x04bd7,0x04ad0,0x0a4d0,0x1d0b6,0x0d250,0x0d520,0x0dd45,
0x0b5a0,0x056d0,0x055b2,0x049b0,0x0a577,0x0a4b0,0x0aa50,0x1b255,0x06d20,0x0ada0,

0x14b63,0x09370,0x049f8,0x04970,0x064b0,0x168a6,0x0ea50,0x06b20,0x1a6c4,0x0aae0, # 2050-2059
0x0a2e0,0x0d2e3,0x0c960,0x0d557,0x0d4a0,0x0da50,0x05d55,0x056a0,0x0a6d0,0x055d4, # 2060-2069
0x052d0,0x0a9b8,0x0a950,0x0b4a0,0x0b6a6,0x0ad50,0x055a0,0x0aba4,0x0a5b0,0x052b0, # 2070-2079
0x0b273,0x06930,0x07337,0x06aa0,0x0ad50,0x14b55,0x04b60,0x0a570,0x054e4,0x0d160, # 2080-2089
0x0e968,0x0d520,0x0daa0,0x16aa6,0x056d0,0x04ae0,0x0a9d4,0x0a2d0,0x0d150,0x0f252, # 2090-2099
0x0d520
]


def solarTerm(y, m, dd, h, n):
    global temp_d0, temp_d1, temp_d2, tempd3  # 0 -> last 如果相同与现在 last就是d3   1->next
    global monthnumberyuegan, monthnumberyuezhi, monthnumberdiff
    global last_jieqiName, next_jieqiName, jieqiName
    temp_y = str(y)
    index = 0

    if m < 10:
        temp_m = '0' + str(m)
    else:
        temp_m = str(m)

    if dd < 10:
        temp_d = '0' + str(dd)
    else:
        temp_d = str(dd)

    if h < 10:
        temp_h = '0' + str(h)
    else:
        temp_h = str(h)

    if n < 10:
        temp_n = '0' + str(n)
    else:
        temp_n = str(n)

    temp_d2 = temp_y + '/' + temp_m + '/' + temp_d + '/' + temp_h + ':' + temp_n
    for i in range(2, 1802): # 4, 1802
        temp_d0 = d[i]
        if temp_d2 >= temp_d0:
            temp_d3 = d[i-1]
            last_jieqiName = jieqi0[(index-1) % 12]
        else:
            last_jieqiName = jieqi0[index%12]

        temp_d1 = d[i+1]
        next_jieqiName = jieqi0[(index+1)%12]

                                  # temp_d2 <= temp_d1
        if temp_d2 >= temp_d0 and temp_d2 < temp_d1:
            temp_sd0 = temp_d0.split('/')
            monthnumberyuegan = (int(temp_sd0[0]) - 1900) * 12 + (int(temp_sd0[1])-7)
            monthnumberyuezhi = (int(temp_sd0[0])- 1900) * 12 + (int(temp_sd0[1])-11)
            # monthnumberdiff = (int(temp_sd0[0]) - 1900) * 12 + (int(temp_sd0[1]) - 2)
            print('temp_d2 输入的公历年月日时: ', temp_d2)
            '''
            if m - 2 < 0:
                jieqiName = jieqi0[m - 2 + 12]
            else:
                jieqiName = jieqi0[m- 2]
            print('节气名: ', jieqiName)
            '''
            print('节气: ', jieqi0[(index) % 12] )
            print('next temp_d1: 下个节气：', temp_d1, next_jieqiName)
            #print('last temp_d0: ', temp_d0, last_jieqiName)
            print('last temp_d3: 上个节气：', temp_d3, last_jieqiName)
            #print(jieqiName)
            break
        index +=1

    yuegan = int(monthnumberyuegan % 10)
    if (yuegan == 0):
        yuegan = 10
    yuezhi = int(monthnumberyuezhi % 12)
    if (yuezhi == 0):
        yuezhi=12


    return tiangan[yuegan-1] + dizhi[yuezhi-1]


#  返回农历y年一整年的总天数
def lYearDays(y):
    i=0x8000
    sum = 348
    while i and i>0x8:
        #if not i>0x8:
        #    break
        temp = (lunarInfo[y - 1900] & i)
        if temp:
            sum += 1
        else:
            sum += 0

        i >>= 1

    # for(i=0x8000; i>0x8; i>>=1)
    # sum = sum+ (lunarInfo[y-1900] & i)? 1: 0;

    return sum + leapDays(y)


# 返回农历y年闰月的天数 若该年没有闰月则返回0
def leapDays(y):
    if leapMonth(y):
        temp = lunarInfo[y-1900] & 0x10000
        if temp:
            return 30
        else:
            return 29
    else:
        return 0



# 返回农历y年闰月是哪个月；若y年没有闰月 则返回0
def leapMonth(y):
    return (lunarInfo[y-1900] & 0xf)



# 返回农历y年m月（非闰月）的总天数，计算m为闰月时的天数请使用leapDays方法
def monthDays(y, m):
    #   if(m>12 || m<1) {return -1}
    if m > 12 or  m < 1:
        return -1

    temp = lunarInfo[y-1900] & (0x10000>>m)
    if temp:
        return 30
    else:
        return 29


def toGanZhiYear(lYear):
    ganKey = (lYear - 3) % 10
    zhiKey = (lYear - 3) % 12
    if ganKey == 0: ganKey = 10     # 如果余数为0则为最后一个天干
    if zhiKey == 0: zhiKey = 12     # 如果余数为0则为最后一个地支
    return tiangan[ganKey - 1] + dizhi[zhiKey - 1]



def Lunar(y, m, d):
    global i
    global leap
    global temp
    global offset1
    offset = int( (y - 1900) * 365 + ((y - 1900) / 4) + d+ wMonthAdd[m - 1] - 31)

    if (not int(y % 4)) and (m <= 2):
        offset = offset - 1

    offset1 = offset

    i = 1900
    while i<2050 and offset>0:
        temp = lYearDays(int(i))
        offset -= temp
        i+=1

    if offset < 0:
        offset += temp
        i-=1

    global year
    year = i
    leap = leapMonth(i)
    global isLeap
    isLeap = False

    i = 1
    while i<13 and offset>0:
        if leap>0 and i==(leap + 1) and isLeap==False:
            i -= 1
            isLeap = True
            temp = leapDays(year)
        else:
            temp = monthDays(year, i)

        if isLeap == True and i == (leap + 1):
            isLeap = False

        offset -= temp
        i+=1

    if offset == 0 and leap > 0 and i == leap + 1:
        if isLeap:
            isLeap = False
        else:
            isLeap = True
            i -= 1

    if offset < 0:
        offset += temp
        i -= 1

    month = i
    day = offset + 1

    # nongligan = int( (year - 1900) % 10 + 7 )
    # nongzhi = int( (year - 1900) % 12 + 1 )

    # if nongligan > 10:
    #     nongligan = nongligan-10
    # if nongzhi > 12:
    #     nongzhi = nongzhi-12

    rigan = int(offset1 % 10)
    rizhi = int(offset1 % 12 + 4)
    if rigan >= 10:
        rigan=rigan-10
    if rizhi >= 12:
        rizhi=rizhi-12

    gzY = toGanZhiYear(year)

    if  nongliyue[month-1] == '腊':
        print('year      农历年份：', y-1)
    else:
        print('year      农历年份：', y)

    # print(month)

    print('month     农历月份：', nongliyue[month-1] + '月')

    print('day       农历日期：', nongliri[day-1])
    #print('nongligan: ', tiangan[nongligan])
    #print('nonglizhi: ', dizhi[nongzhi])
    print('gzY         年干支：', gzY)
    print('rigan+rizhi 日干支：', tiangan[rigan] +  dizhi[rizhi])
    #print('rizhi', dizhi[rizhi])


tianganNum={"甲": 1, "乙": 2, "丙": 3, "丁": 4, "戊": 5, "己": 6, "庚": 7, "辛": 8, "壬": 9, "癸": 10}
dizhiNum={'子': 1, "丑": 2, "寅": 3, "卯": 4, "辰": 5, "巳": 6, "午": 7, "未": 8, "申": 9,"酉": 10, "戌": 11, "亥": 12}
shiZhiStr={23:'子', 24:'子', 0: '子', 1: '丑', 2: '丑', 3: '寅', 4: '寅', 5: '卯', 6: '卯', 7: '辰', 8: '辰', 9: '巳',
           10: '巳', 11: '午', 12: '午', 13: '未', 14: '未', 15: '申', 16: '申', 17: '酉', 18: '酉', 19: '戌', 20: '戌',
           21: '亥', 22: '亥'}


def setShiGanZhi(ch, riGanZhi):
    riGanNum = tianganNum[riGanZhi[0]]
    # riZhiNum = dizhiNum[riGanZhi[1]]
    shiZhiNum = dizhiNum[shiZhiStr[int(ch)]]
    shiGanZhi = tiangan[(riGanNum * 2 + shiZhiNum -2) % 10 -1] + shiZhiStr[int(ch)]
    print('shiGanZhi   时干支：', shiGanZhi)
    #shiGanNum = (riGanNum * 2 + shiZhiNum -2) % 10
    # shiGanNum = riGanNum*2 +

# 1900 - 2050
Lunar(2017, 3, 5)
print("yueganzhi   月干支：", solarTerm(2017, 3, 5, 23, 40))

setShiGanZhi(14, '丁亥')



# 2017年惊蛰时间：3月5日 17:32:40，农历2017年二月(大)初八
# 因为节气划分只定位到分钟，所以输入是17.32就还是壬寅月，
# 因为真正距离到下个月还有40秒
# 快速推算時柱干支法 推算公式：

# ①日幹x2+時支數-2=時幹數(時幹數超過10要遞減10，只取個位數o)
# ②時支是固定的，時辰順序是：子時、丑時、寅時、卯時、辰時、巳時、午時、未時、申時、酉時、戌時、亥時。
# 例一：求乙卯日巳時的干支
# 已知日幹“乙”爲2，時支“巳”爲6代入公式：2x2+6—2=8，天干數8是“辛”。
# 則知乙卯日巳時的干支的“辛巳”。
# 例二：求己醜日寅時的干支
# 已知日幹“己”爲6，時支寅爲3代入公式：6x2+3—2＝13，13—10＝3，天干數3是“丙”。 則知己醜日寅時的干支爲“丙寅”。
'''
二进制形式
xxxx	xxxx	xxxx	xxxx	xxxx
20-17	16-12	12-9	8-5	    4-1
1-4: 表示当年有无闰年，有的话，为闰月的月份，没有的话，为0。
5-16：为除了闰月外的正常月份是大月还是小月，1为30天，0为29天。
注意：从1月到12月对应的是第16位到第5位。
17-20： 表示闰月是大月还是小月，仅当存在闰月的情况下有意义。
举个例子：
1980年的数据是： 0x095b0
二进制：0000 1001 0101 1011 0000
表示1980年没有闰月，从1月到12月的天数依次为：30、29、29、30、29、30、29、30、30、29、30、30。
1982年的数据是：0x0a974
0000 1010 1010 0111 0100
表示1982年的4月为闰月，即有第二个4月，且是闰小月。
从1月到13月的天数依次为：30、29、30、29、29(闰月)、30、29、30、29、29、30、30、30。
'''
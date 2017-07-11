# -*-coding:utf-8 -*-
import requests
import re
import math
from app import connection
from tutorial.myLogger import MyLogger


# 获取开奖信息并写入数据库
def get_kjhm(page):
    url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_" + str(page) + ".html"
    headers = {"accept": "application/json, text/plain, */*",
               "Accept-Encoding": "gzip, deflate, sdch, br",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, "
                             "like Gecko) Chrome/58.0.3029.110 Safari/537.36"
               }
    # 获得dom
    content = requests.get(url, headers=headers, data=None, timeout=10).text
    temp_rows = content.split('table')[1].split('/tr')
    logger = MyLogger('kajm_sql')
    for info in temp_rows:
        try:
            kjrq, qh, secend_temp = re.findall('''<td align="center">(.*?)</td>''', info)
            secend = re.findall('''>(\d+)<''', secend_temp)[0]
        except Exception as e:
            print(e)
            continue
        num1, num2, num3, num4, num5, num6, num7 = re.findall('''>(\d+)</em>''', info)
        sales, first = re.findall('''<strong>(.*?)</strong>''', info)

        sql = "INSERT INTO `duan`.`kjhm`(`qh`, `kjrq`, `num1`, `num2`, `num3`, `num4`, `num5`, `num6`, `num7`, " \
              "`sales`, `first`, `secend`) values (%d, %s, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)" % \
              (int(qh), kjrq.replace('-', ''), int(num1), int(num2), int(num3), int(num4), int(num5), int(num6),
               int(num7), int(sales.replace(',', '')), int(first), int(secend))
        logger.info(sql)
        # 写入数据库
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
            cursor.close()


def get_weathar(date_time):
    url = "http://www.tianqihoubao.com/lishi/beijing/month/" + date_time + ".html"
    headers = {"accept": "application/json, text/plain, */*",
               "Accept-Encoding": "gzip, deflate, sdch, br",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, "
                             "like Gecko) Chrome/58.0.3029.110 Safari/537.36"
               }
    try:
        content = requests.get(url, headers=headers, data=None, timeout=10).text
    except Exception as e:
        print(e)
    temp_rows = content.split('table')[1].split('/tr')
    logger = MyLogger('weathar_sql')
    for info in temp_rows:
        try:
            rq = re.sub('\D', "", re.findall('\d+年\d+月\d+日', info)[0])
            temp_wd = re.findall('''(-?\d+)℃''', info)
            wd = math.floor((int(temp_wd[0]) + int(temp_wd[1]))/2)
            desc = get_desc(info)
            if desc == "鬼天气":
                logger.info("="*10)
                logger.info(info)
                logger.info("="*10)
        except Exception as e:
            print(e)
            continue
        sql = "INSERT INTO `duan`.`weathar` (`rq`, `desc`, `wd`) values ('%s', '%s', %d)" % (rq, desc, wd)
        logger.info(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
            cursor.close()


def get_desc(info):
    if "雨" in info:
        if "小雨" in info:
            return "小雨"
        elif "中雨" in info:
            return "中雨"
        elif "阵雨":
            return "阵雨"
        else:
            return "大雨"
    elif "多云" in info:
        return "阴"
    elif "阴" in info:
        return "阴"
    elif "晴" in info:
        return "晴"
    elif "雪" in info:
        if "小雪" in info:
            return "小雪"
        elif "中雪" in info:
            return "中雪"
        else:
            return "大雪"
    elif "雾" in info:
        return "雾"
    else:
        return "鬼天气"








def test():
    pass


if __name__ == '__main__':
    for i in range(2011, 2018):
        for j in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
            month = str(i) + j
            get_weathar(month)


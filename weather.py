#! /usr/bin/python
# -*- coding:utf-8 -*- 

import urllib.request
import re

def get_html():

    city = input("输入城市(拼音): ")
    #url = "http://php.weather.sina.com.cn/search.php?city=" + city + "&dpc=1"
    url = "http://weather.sina.com.cn/" + city
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
    headers = {"User-Agent": user_agent}

    request = urllib.request.Request(url=url, data=None, headers=headers)
    response = urllib.request.urlopen(request)

    get_html = response.read()
    get_html = get_html.decode("utf-8")

    return get_html

def get_weather_info(get_html):

    re_city   = r"<h4.*id.*slider_ct_name.*>(.*)</h4>"
    re_date   = r"<p.*slider_ct_date.*>(.*)</p>"
    re_time   = r"<div.*slider_ct_time.*title.*>(.*)</div>"
    re_degree = r"<div.*slider_degree.*>(.*)</div>"
    re_detail = r"<p.*slider_detail.*\n.*</p>"
    re_plt    = r"<div.*slider_warn_i_tt.*\n.*\n.*\n.*</div>"

    city   = re.search(re_city,   get_html)
    date   = re.search(re_date,   get_html)
    time   = re.search(re_time,   get_html)
    degree = re.search(re_degree, get_html)
    detail = re.search(re_detail, get_html)
    plt    = re.search(re_plt,    get_html)

    if (city   != None and 
        date   != None and
        time   != None and
        degree != None and
        detail != None and
        plt    != None):

        str_city = city.group(0)
        str_city = str_city[str_city.find(">")+1 : str_city.rfind("<")]

        str_date = date.group(0)
        str_date = str_date[str_date.find(">")+1 : str_date.rfind("<")]

        str_time = time.group(0)
        str_time = str_time[str_time.find(">")+1 : str_time.rfind("<")]

        str_degree = degree.group(0)
        str_degree = str_degree[str_degree.find(">")+1 : str_degree.rfind("&#8451;")]

        str_detail = detail.group(0)
        str_detail = str_detail[str_detail.find(">")+1 : str_detail.rfind("<")].replace("&nbsp;", "").replace("|", "").replace("                            "," ").strip()

        str_plt = plt.group(0)
        str_plt = str_plt[str_plt.find("<p>")+len("<p>") : str_plt.rfind("</p>")]
        
        print("========================")
        print("城市: %s\n日期: %s\n时间: %s\n温度: %s\n详情: %s\n污染: %s" % 
               (str_city, str_date, str_time, str_degree, str_detail, str_plt))
        print("========================")

    else:
        print("Something Error")

def get_weather():
    get_weather_info(get_html())


get_weather()


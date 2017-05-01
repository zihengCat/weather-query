#! /usr/bin/python
# -*- coding:utf-8 -*- 

import urllib.request
import re

def get_weather():

    city = input("输入城市(拼音): ")
    #url = "http://php.weather.sina.com.cn/search.php?city=" + city + "&dpc=1"
    url = "http://weather.sina.com.cn/" + city
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
    headers = {"User-Agent": user_agent}
    request = urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    get_html = response.read()
    get_html = get_html.decode("utf-8")


    # process city name
    re_city  =  r"<h4.*id.*slider_ct_name.*>(.*)</h4>"
    title = re.search(re_city, get_html)
    if (title != None):
        target_str = title.group(0)
        print("城市: %s" % 
              target_str[target_str.find(">")+1 : target_str.rfind("<")])
    else:
        print("No match in city")

    # process query time
    re_time = r"<p.*slider_ct_date.*>(.*)</p>"
    time = re.search(re_time, get_html)
    if (time != None):
        target_str = time.group(0)
        print("日期: %s" %
              target_str[target_str.find(">")+1 : target_str.rfind("<")])
    else:
        print("No match in time")

    # process query detail time
    re_dtime = r"<div.*slider_ct_time.*title.*>(.*)</div>"
    dtime = re.search(re_dtime, get_html)
    if (dtime != None):
        target_str = dtime.group(0)
        print("时间: %s" %
              target_str[target_str.find(">")+1 : target_str.rfind("<")])
    else:
        print("No match in dtime")

    # process temperature
    re_degree = "<div.*slider_degree.*>(.*)</div>"
    we_degree = re.search(re_degree, get_html)
    if (we_degree != None):
        target_str = we_degree.group(0)
        print("温度: %s" %
              target_str[target_str.find(">")+1 : target_str.rfind("&#8451;")])
    else:
        print("No match in temperature")

    # process temperature detail
    re_ddegree = "<p.*slider_detail.*\n.*</p>"
    we_ddegree = re.search(re_ddegree, get_html)
    if (we_ddegree != None):
        target_str = we_ddegree.group(0)
        print("详情: %s" % 
              target_str[target_str.find(">")+1 : target_str.rfind("<")].replace("&nbsp;", "").replace("|", "").replace("                            "," ").strip())
    else:
        print("No match in temperature detail")


     # process Pollution
    re_plu = "<div.*slider_warn_i_tt.*\n.*\n.*\n.*</div>"
    we_plu = re.search(re_plu, get_html)
    if (we_plu != None):
        target_str = we_plu.group(0)
        print("污染: %s" % 
              target_str[target_str.find("<p>")+len("<p>") : target_str.rfind("</p>")])
    else:
        print("No match in pollution")

get_weather()


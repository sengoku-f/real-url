# 获取易车直播的真实流媒体地址，默认最高画质。
# http://live.yiche.com/live/58911.html
import sys
import requests
import re


# 获取传入参数
live_id = re.search(r'[a-zA-z]+:\/\/[^\s]*yiche\.com[^\s]*\/(\d+)\.html[^\s]*', sys.argv[1]).group(1)

live_url = "http://live.yiche.com/web/pc/live/ShowIframe?liveid={}&viewname=IframeNormShow&support=1&dm=1".format(live_id)

# r = requests.get(live_url)

s = re.search(r'\/\/[^\s]*\.(m3u8|mp4)', requests.get(live_url).text).group()

# 打印真实链接
print('http:' + str(s))

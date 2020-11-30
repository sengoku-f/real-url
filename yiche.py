# 获取易车直播的真实流媒体地址，默认最高画质。
# http://live.yiche.com/live/58911.html

import requests
import re

def get_real_url(url):
  # 获取传入参数
  live_id = re.search(r'[a-zA-z]+:\/\/[^\s]*yiche\.com[^\s]*\/(\d+)\.html[^\s]*', url).group(1)

  live_url = "http://live.yiche.com/web/pc/live/ShowIframe?liveid={}&viewname=IframeNormShow&support=1&dm=1".format(live_id)

  s = re.search(r'\/\/[^\s]*\.(m3u8|mp4)', requests.get(live_url).text).group()

  # 打印真实链接
  return 'http:' + s

if __name__ == '__main__':
    url = input('输入易车直播链接：\n')
    print(get_real_url(url))
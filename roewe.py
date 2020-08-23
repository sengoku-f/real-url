# 获取荣威直播的真实流媒体地址，默认最高画质。

import sys
import requests
import re


# 获取传入参数
roewe_url = re.search(r'([a-zA-z]+:\/\/[^\s]*roewe\.com[^\s]*\/)index\.html[^\s]*', sys.argv[1]).group(1) + 'js/parameter.js'

r = requests.get(roewe_url)
live_id = re.search(r'var\ssaicLiveId\s=\s\'(\d+)\';', (r.text)).group(1)

live_url = "https://live.vhall.com/webinar/inituser/{}?embed=video".format(live_id)

s = re.search(r'\/\/[^\s]*record\.m3u8', requests.get(live_url).text).group()

# 打印真实链接
print('http:' + str(s))

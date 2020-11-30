# 获取荣威直播的真实流媒体地址，默认最高画质。
# 直播链接
# https://www.roewe.com.cn/about-us/new&activity/html/activity/live/RSHBund/share/index.html?channel=wechat&macAddress=159680031632671805&userId=10000003755407&shareTime=1597287406050&from=singlemessage-

import requests
import re

def get_real_url(url):
  # 获取传入参数
  roewe_url = re.search(r'([a-zA-z]+:\/\/[^\s]*roewe\.com[^\s]*\/)index\.html[^\s]*', url).group(1) + 'js/parameter.js'

  r = requests.get(roewe_url)
  live_id = re.search(r'var\ssaicLiveId\s=\s\'(\d+)\';', (r.text)).group(1)

  live_url = "https://live.vhall.com/webinar/inituser/{}?embed=video".format(live_id)

  s = re.search(r'\/\/[^\s]*record\.m3u8', requests.get(live_url).text).group()

  # 返回真实链接
  return 'http:' + s

if __name__ == '__main__':
    url = input('输入荣威直播链接：\n')
    print(get_real_url(url))


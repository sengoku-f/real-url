#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import douyin
import sys


if __name__ == '__main__':
    url = douyin.get_real_url(sys.argv[1])[1]
    print(url)
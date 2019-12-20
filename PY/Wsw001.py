#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

try:
    os.mkdir("wangsw")
except FileExistsError:
    print("你创不了")
print("111")


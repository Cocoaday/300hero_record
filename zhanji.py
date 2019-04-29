#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
import baseinfo

# 判断运行系统
sys = platform.system()

# 读取ID
try:
	IDfile = open('ID.txt','r')
	ID = IDfile.read()
	if sys == 'Windows':
		print ID.decode('utf-8').encode('gbk')
	else:
		print ID
	baseinfo.baseinfo(ID)
finally:
	if IDfile:
		IDfile.close()
	
# with open('output.txt', 'w') as outp:
    # outp.write(ID)
    # outp.close()
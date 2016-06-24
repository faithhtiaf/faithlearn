#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import urllib
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# #
# file=open("C:\inverst_compName.txt",'r')
# list=file.readlines()
#  u'上海交大慧谷通用技术有限公司', u'重庆易极付科技有限公司', u'重庆秒差距科技有限公司',u'智者四海（北京）技术有限公司',\
#                        u'重庆猪八戒网络有限公司',\
#                        # u'重庆易宠科技有限公司',u'0',u'重庆安海科技有限公司',u'上海福美来房地产经纪有限公司',u'重庆渝宁化肥有限公司',u'东软集团股份有限公司'
url= 'http://192.168.31.116:9030/company/profile/statistic'
comp_name_lst = [u'杭州誉存科技有限公司']
res=requests.post(url, data=json.dumps({'companyNameList':comp_name_lst, 'slice':7}))
# list=[u'   北京奇虎360科技有限公司',]
#  di={'companyNameList':list}
#  url=""

# res=requests.post(url,data=json.dumps(di))

print res.content
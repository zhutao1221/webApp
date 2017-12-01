# -*- coding: utf-8 -*-
import requests
import json
idata = json.dumps({'text': '你好'})
iheaders = {'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Content-Length':'13',
            'Content-Type':'application/json',
            'Cookie':'sessionid=8fd06yn0n27w99es55j3nx8qsshbdio1; csrftoken=cXjVhrqmNfUk8bvtpybUmwnDKh9JqV49PzRwB4JAiSOGmGNnatz6WGS5Vg2dZAIn',
            'Host':'127.0.0.1:8000',
            'Origin':'http://127.0.0.1:8000',
            'Referer':'http://127.0.0.1:8000/',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'X-CSRFToken':'undefined',
            'X-Requested-With':'XMLHttpRequest'          
           }
r = requests.post('http://127.0.0.1:8000/MachineLearningService/', data=idata, headers=iheaders) 
print(r.text)
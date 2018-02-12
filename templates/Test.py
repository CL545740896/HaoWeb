# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import httplib
import urllib
import random


def send_sms(text, mobile):
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 用户名是登录用户中心->验证码短信->产品总览->APIID
    account = "C27266444"
    # 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
    password = "146accbed96f35e016a4b7de6b2e8012"
    params = urllib.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


def getCode():
    code = ''
    s = []
    while (len(s) < 4):
        x = random.randint(0, 9)
        if x not in s:
            s.append(x)
            code = code + str(x)
    return code

print u"\u540c\u4e00\u624b\u673a\u53f7\u9a8c\u8bc1\u7801\u77ed\u4fe1\u53d1\u9001\u8d85\u51fa5\u6761"
# if __name__ == '__main__':
#     mobile = "13750011737"
#     text = "您的验证码是：" + getCode() + "。请不要把验证码泄露给其他人。"
#     print(send_sms(text, mobile))
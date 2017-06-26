#!usr/bin/env python

# coding:utf-8
"""
create on
 author:whycwen

"""




import urllib.request
import urllib.parse
if __name__ == '__main__':

    url = "http://www.maiziedu.com"
    #测试开源中国网的登录测试
    #点击登录按钮 是的url 并把 用户数据使用post 提交到服务器
    url_oschina = 'https://www.oschina.net/action/user/hash_login?from='
    values = {'email':'abcd.@cc.com','pwd':'1234567'}
    data = urllib.parse.urlencode(values).encode('utf-8')
    #通常情况下都要设置头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    req = urllib.request.Request(url_oschina, data=data,headers=headers)
    response = urllib.request.urlopen(req)
    #读取响应内容
    html = response.read()
    #解码输出
    print(html.decode('utf-8'))
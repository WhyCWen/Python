import  urllib.request
import  urllib.parse

url = ' http://www.qiushibaike.com/textnew/page/2/?s=4994647'
user_agent={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
values = {}
data = urllib.parse.urlencode(values).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=user_agent)
respond = urllib.request.urlopen(request)
content = respond.read().decode('utf-8')
print(content)
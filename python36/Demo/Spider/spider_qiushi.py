#!usr/bin/env python
#coding : 'utf-8'
#author : whycwen

# """
#  要求抓取 糗事百科的 新鲜事 的文本内容
#  实现步骤分析:
#  使用面向对象的方式
#  1,访问网页 ,获取源代码
#  2,源代码分析
#  3,存储爬取的数据
#
# """

######
import  urllib.request
import  urllib.parse
import  re
import  os


class Spider(object):
    #初始化 构造器
    # def __int__(self,regex,url,user_agent):
    #     # 作为全局变量时 不能使用该变, 此问题待解决????
    #     self.regex = regex
    #     self.url = url
    #     self.user_agent = user_agent

    def set_regex(self,regex):
        self.regex = regex
    def set_url(self,url):
        self.url = url
    def set_user_agent(self,user_agent):
        self.user_agent = user_agent

    def set_all(self,regex=None,url='',user_agent={''}):
        self.regex = regex
        self.url = url
        self.user_agent = user_agent

    #获取网页数据
    def get_page(self,page_index):
        try:
            #values = {}
            #data = urllib.parse.urlencode(values).encode('utf-8')
            request = urllib.request.Request(url=self.url%str(page_index),headers=self.user_agent)
            respond =  urllib.request.urlopen(request)
            content = respond.read().decode('utf-8')
            return  content
        except Exception as e:
            print("网页打开错误",e)
        return  ''
    #分析数据 提取有用数据
    def analyzing(self,content):
        if self.regex is None:
             regex = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
        else:
            regex =self.regex
        pattern = re.compile(regex,re.S)
        items = re.findall(pattern,content)
        return  items
    def save(self,items,path,file_name):
        try:
            if not os.path.exists(path):
                os.mkdir(path)
            file_path = path + '/' + file_name
            with open(file_path, 'a', encoding='utf-8') as f:
                try:
                    for item in items:
                        f.write(item.replace('<br/>','\n')+'\n\n')
                except IOError:
                    print('文件写入错误')
                finally:
                    f.close()
        except IOError:
            print("文件打开错误")

    def run(self,path='qiushi',file_name='qiushi.txt'):
        print('开始抓取数据\%')
        file_path = path + '/' + file_name
        if os.path.exists(file_path):
            try:
                with open(file_path, 'w') as f:
                    try:
                        f.write('')
                    except IOError:
                        print ("write file error")
                    finally:
                        f.close()
            except IOError:
                print ('file open error')
        for i in  range(1,8):
            content = self.get_page(i)
            items = self.analyzing(content)
            self.save(items,path,file_name)
    def run_qiushi_textnew(self):
        self.run()
if __name__ == '__main__':

    url = 'http://www.qiushibaike.com/textnew/page/%s/?s=4994647'
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    regex = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    sipder = Spider()
   # sipder.set_regex(regex)
    sipder.set_user_agent(user_agent)
    sipder.set_url(url)
    sipder.run_qiushi_textnew()
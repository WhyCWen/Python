#!usr/bin/env python
#coding : 'utf-8'
#author : whycwen

"""
python`s version is 2.7

"""
import  urllib2
import  re
import  os


class Spider(object):

    def __int__(self):

        self.url ='http://www.qiushibaike.com/textnew/page/2/?s=4994647'
        self.user_agent={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}


    def get_page(self,page_index):
        url = 'http://www.qiushibaike.com/textnew/page/%s/?s=4994647'%str(page_index)
        user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
        try:
            request = urllib2.Request(url=url,headers=user_agent)
            respond =  urllib2.urlopen(request)
            content = respond.read()
            return  content
        except urllib2.HTTPError as e:
            print 'http request error'
        except urllib2.URLError as e:
            print 'URL address error'
        except:
            print "get web page others error"
        return  ''

    def analyzing(self,content):
        regex = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
        pattern = re.compile(regex,re.S)
        items = re.findall(pattern,content)
        return  items

    def save(self,items,path):
        try:
            if not os.path.exists(path):
                os.mkdir(path)
            file_path = path + '/' + 'quishi.txt'
            with open(file_path, 'a') as f:
                try:
                    for item in items:
                        item_new = item.replace('<br/>', '\n')
                        f.write(item_new+'\n\n\n')
                except IOError:
                    print '123'
                except Exception as e:
                    print e
                finally:
                    f.close()
        except IOError:
            print '12456'

    def run(self):
        path = 'qiushi'
        file_path = path +'/' + 'quishi.txt'
        if os.path.exists(file_path):
            try:
                with open(file_path, 'w') as f:
                    try:
                        f.write('')
                    except IOError:
                        print "write file error"
                    finally:
                        f.close()
            except IOError:
                print 'file open error'
        for i in  range(1,5):
            content = self.get_page(i)
            items = self.analyzing(content)
            self.save(items,path)
if __name__ == '__main__':
    sipder = Spider()
    sipder.run()
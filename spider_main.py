#!/usr/bin/env python
# -*- coding: utf-8 -*-
from spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManger()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    
    
    def craw(self, root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:#加入异常处理
                new_url=self.urls.get_new_url()
                print'craw %d:%s'%(count,new_url)
                html_cont=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parser(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count==100:#加入限制，这里只爬取1k个页面
                    break
                count=count+1
            except:
                print'craw failed'
        #如果有new url，提取，下载，解析，然后保存解析出的新url，输出收集到的数据
        self.outputer.output_html()
    
    



if __name__=="__main__":
    root_url="https://baike.baidu.com/item/Python/407313"
    #入口url
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
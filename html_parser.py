#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from urlparse import urljoin

class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls=set()
        #知道需要提取的url形式为/item/Web/150564
        links=soup.find_all('a',href=re.compile(r"/item/"))
        for link in links:
            new_parse_url=link['href']
            #如果提取到的是不完整url，需要合成完整url
            new_full_url=urljoin(page_url,new_parse_url)
            new_urls.add(new_full_url)
        return new_urls
        
    
    
    def _get_new_data(self, page_url, soup):
        res_data={}
        
        #w为方便使用，将url也放入数据中
        res_data['url']=page_url
        
        #匹配title节点
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>@@@</h1>
        title_node=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title']=title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node=soup.find('div',class_="lemma-summary")
        res_data['summary']=summary_node.get_text()
        
        return res_data
        
    
    
    def parser(self,new_url,html_cont):
        if new_url is None or html_cont is None:
            return
        
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(new_url,soup)
        new_data=self._get_new_data(new_url,soup)
        return new_urls,new_data
    
    




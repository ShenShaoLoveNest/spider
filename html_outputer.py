#!/usr/bin/env python
# -*- coding: utf-8 -*-

class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout=open('output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border=\"1\">")#数据输出为表格形式
        
        #需要注意python默认输出ascii，需转换utf-8
        for data in self.datas:
            fout.write("<tr>")#行
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            fout.write("</tr>")
            


        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()
    
    
    
    




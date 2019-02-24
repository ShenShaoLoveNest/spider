# spider
一个spider实战程序，功能是爬取百度百科python页面的相关100个页面的url，title，summary


需要的东西：
简单爬虫架构知识
url管理器
网页下载器（urllib2）
网页解析器（BeautifulSoup）

简单爬虫结构：
爬虫调度端→URL管理器→网页下载器→网页解析器→价值数据

URL管理器：管理待抓取URL集合和已抓取URL集合
          防止重复抓取，防止循环抓取
网页下载器：urllib2：python官方基础模块
           requests：第三方包，更强大
urllib2下载方法：1，response=urllib2.urlopen(url)
                   print response.getcode()#200表示成功
                   cont=response.read()#读取内容
                2，添加data，http header
                   request=urllib2.Request(url)#创建Request对象
                   request.add_data('a','1')#添加数据
                   request.add_header('User-Agent','Mozilla/50')
                   response=urllib2.urlopen(url)
                3,添加特殊情景的处理器
                   import urllib2,cookielib#增加cookie模块
                   cj=cookielib.CookieJar()#创建cookie容器
                   opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                   #创建一个opener
                   urllib2.install_opener(opener)#给urllib2安装opener
                   response=urllib2.urlopen(url)
实例演示：1，创建project，选择PyDev Project
         2，创建package
         3，创建module：xxx_urllib2

实例分析：目标：需要爬取的目标
         入口页：目标网页
         url格式：页面url：/view/1234.htm
         数据格式：标题:/item/Web/150564
                  简介:<dd class="lemmaWgt-lemmaTitle-title"><h1>@@@</h1>
         页面编码：UTF-8

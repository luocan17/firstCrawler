# firstCrawler
第一个Python爬虫，当时陪陈名去三号院当助教。

crawl.py的功能：解析./2018MHRBD/saomiao/目录下所有文档中的url，获取学信网学生信息。

过程：首先获取网页源代码存放在./2018MHRBD/html/中，然后根据一定
的规则获取相关信息，将结果存放在./2018MHRBD/result/目录中。

要查找姓名等信息，除了crawl.py中的方法外，还可通过正则表达式来实现：

import re

...

reg = r'名：<span class="songTi">(.*)</span>' #正则表达式，(.*)是一个子表达式

reg_name = re.compile(reg)#编译一下，运行更快

list = reg_name.findall(html)#进行匹配，html待匹配的网页源码

for name in list:

    print name

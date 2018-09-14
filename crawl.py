#--encoding=utf8
#! /usr/bin/python
__author__ = 'huosan'

import StringIO
import re
from lxml import etree
from lxml.html import document_fromstring
import time
import os
import urllib2
import csv
import sys
import stat
import shutil


def saveList(lista,savepath,writype='w'):
    writer = csv.writer(file(savepath,writype))
    for line in lista:
        if line:
            writer.writerow(line)          
            
    
def createFolder(folderName,keepold=True):
    if keepold and os.path.isdir(folderName):
        print folderName,'have existed'
    else:
        if os.path.isdir(folderName):
            shutil.rmtree(folderName)
#                 os.removedirs(folderName)
        os.makedirs(folderName)
        os.chmod(folderName,stat.S_IREAD|stat.S_IWRITE)
#             subFileChmod(folderName, stat.S_IREAD|stat.S_IWRITE)
    return folderName
    
    
# class Comment(DynamicDocument):
#     _pid = StringField()
#     _uID = StringField()
#     _uRank = StringField()
#     _uVote = StringField()
#     _commentDate = StringField()
#     _bDate = StringField()
# 
# class price(DynamicDocument):
#     _pid = StringField()
#     _date = StringField()
#     _price = StringField()

def fetch(link):
    buf = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, link)
    c.setopt(pycurl.WRITEFUNCTION, buf.write)
    c.perform()
    return buf


def tohtml(htmlelement):
    return etree.tostring(htmlelement, encoding='utf-8')


def tostring(htmlelement):
    return htmlelement.text_content().encode('utf-8')


def extractPriceHis(buf):
#     pricehis=''
    doc=document_fromstring(buf)
    pircehis = doc.xpath("/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[1]")
    mass = tostring(pircehis[0]).replace('\n','')
    print mass
    er
#     print mass,'\n\n抽取待续...'
#     mass=r'ajksp aintchartdhfkdju});i'
    prefix='\['
    sufix='\]'
#    patt=str("^"+prefix+".*(?<!\\."+sufix+")$")
    patt = '\\[(.*?)\\]'
#     print patt
    return re.findall(patt,mass) #re.compile(r"([j]+*[ui])")
    
    

    

def saveComments(comments):
    for x in comments:
        x.save()

def savehtml(html,filename):    
    f=open(filename,'w')
    f.write(html)
    f.close()

workfolder = ".\\2018MHRBD\\"
xs,errorinfo = [],[]
workfolder_url = workfolder+"saomiao\\"
workfolder_html = createFolder(workfolder+"html\\")
workfolder_res = createFolder(workfolder+"result\\")

for fp in os.listdir(workfolder_url):
    #fp = 'B.txt'
    print fp," starting-------------------------"
    fpname = os.path.splitext(fp)[0]
    if not os.path.isfile(workfolder_url+fp):
        continue
    filep = open(workfolder_url+fp)
    #ftxt = filep.read()
    i = 0
    for url in filep:
        i +=1
        print i,url
        url = url.replace('\n','')
        print "capturing...",url
        # if 1:
        try:
            urlid = url.split('=')[-1]
            #urlid = urlid.replace('\n','')
            #print "capturing...",urlid
            
            #print url
            out_path = workfolder_html+fpname+'_'+urlid+'.html'#'./test.html'
            
            #req = urllib2.Request(url, None)
            handle = urllib2.urlopen(url)
            #print handle.info()
            html = handle.read()
            savehtml(html,out_path)
            
        #     html=open(out_path).read()
            
            # print html
            xp_name = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[1]"
            xp_gender = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[2]"
            xp_birth = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[3]"
            xp_xltype = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[4]"
            xp_cc = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[5]"
            xp_school = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[6]"
            xp_majorname = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[7]"
            xp_xzh = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[8]"
            xp_rxdate = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[9]"
            xp_bydate = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[10]"
            xp_bjy = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[11]"
            xp_cetnum = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[1]/span[12]"
         
            doc=document_fromstring(html)
            
            name = tostring(doc.xpath(xp_name)[0])
            gender = tostring(doc.xpath(xp_gender)[0])
            birth = tostring(doc.xpath(xp_birth)[0])
            xltype = tostring(doc.xpath(xp_xltype)[0])
            cc = tostring(doc.xpath(xp_cc)[0])
            school = tostring(doc.xpath(xp_school)[0])
            majorname = tostring(doc.xpath(xp_majorname)[0])
            xzh = tostring(doc.xpath(xp_xzh)[0])
            rxdate = tostring(doc.xpath(xp_rxdate)[0])
            bydate = tostring(doc.xpath(xp_bydate)[0])
            bjy = tostring(doc.xpath(xp_bjy)[0])
            cetnum = tostring(doc.xpath(xp_cetnum)[0])
            
            xp_img = "/html/body/div[4]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[3]/div/div[2]/div/img/@src"
            imgurl = doc.xpath(xp_img)[0]
            
            x = [urlid,name,gender,birth,xltype,cc,school,majorname,xzh,rxdate,bydate,bjy,cetnum,url,imgurl]
            xs.append(x)
            
            #print imgurl
            
            #imgurl = "https://xlrz2.chsi.com.cn/images/qrcode/4ca0s9f0ysek16k1.jpg"
    #         COOKIE='lzstat_uv=31759684842455384331|2893156; SINAGLOBAL=1380028950516.1345.1359677783386; __utma=182865017.1892075838.1369364647.1369364647.1377512904.2; wvr=5; SUS=SID-1676895690-1397859250-XD-d42mk-2c289d9f4f919872a8ff0586beeaef20; SUE=es%3D270e69e28520d9f56a89489738ab0295%26ev%3Dv1%26es2%3D2fffe3dcde023f7bcfd916376d9200e5%26rs0%3DgblVbeWVdKMWgRtfp2dPbSb%252FxFOtqS2AuxQzCFrsNZ5Od%252FxWZCSt2muaxNuigkLoZAE6v%252FIUAsXyo7tHhXbl%252BAmcQtk0m8z9CEwb1t57hs4L2HYzbTHmmRf3vt9%252BC0qbCgIiMhT3durKqR%252B9NPfsHgeIF1m4rIu2RjYnoxypqIs%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1397859250%26et%3D1397945650%26d%3Dc909%26i%3D744a%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D1676895690%26name%3Dkainan.cui%2540live.cn%26nick%3D%25E6%25B1%259F%25E8%25BE%25B9%26fmp%3D%26lcp%3D; SUB=Ae7gsEiYwCCgdkwTKwgvSYv7VUU9hlxiS5IwknxWSpbsyWFLF9Hhk%2BBiyaPjoGkkj0JPHd9iXRQn5WR%2BdHkEF7gWU%2F8bm0TjyjZ6fZxiw1KCE9gH7411gbuxN33gLG9b%2BgKHSVwlaym83ukpuXHZ5xo%3D; SUBP=002A2c-gVlwEm1uAWxfgXELuuu1xVxBxAuhR8fQsVp5ovGEQdRKCVjCuHY-u_E%3D; ALF=1429395249; SSOLoginState=1397859250; NSC_wjq_txfjcp_mjotij=ffffffff094113d745525d5f4f58455e445a4a423660; _s_tentry=login.sina.com.cn; Apache=543959136120.97504.1397859261565; ULV=1397859261654:946:30:11:543959136120.97504.1397859261565:1397809769178; UOR=,weibo.com,login.sina.com.cn'
    #         HEADERS = {"cookie": COOKIE}
    #         
    #         #url="http://s.weibo.com/weibo/%25E7%2594%25B5%25E5%25AD%2590%25E7%2583%259F&timescope=custom:2013-7-11:2013-7-11"
    #         txheaders =  {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', }
    #         
    #         req = urllib2.Request(imgurl, None, txheaders)
    #         handle = urllib2.urlopen(req)
    #         #print handle.info()
    #         html = handle.read()
    #         savehtml(html,workfolder+"html\\"+urlid+'.jpg')    
    
            saveList(xs,workfolder_res+fpname+'-results.csv','a+') 
            xs = []   
        except:
            errorinfo.append([url])
            saveList(errorinfo,workfolder+"errorUrls.txt",'a+')
            errorinfo = []
            print 'XXXXXXXXXXXXXXXXXXXXXXX Has error in:',url
    print fp,"finished=============================="
print "All tasks have finished at ",time.asctime()


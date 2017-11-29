#-*- coding: utf-8 -*-
s = u"今天天气很好。".encode('utf-8')
print type(s)
with open('temp.txt','w') as outputfile:
    outputfile.write(s)
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import urllib,urllib2
# import requests
# from bs4 import BeautifulSoup
# junshi_url="http://mil.qq.com/mil_index.htm"
# proxy = urllib2.ProxyHandler({'https': '47.91.78.201:3128'})
# opener = urllib2.build_opener(proxy)
# opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30')]
# urllib2.install_opener(opener)
# with open('tengxunjunshi2.txt','w') as outputfile:
#    web_page=requests.get(junshi_url).text
#    soup=BeautifulSoup (web_page,'html.parser')
#    junshixinwen=soup.find_all(class_='linkto')
#    for n in junshixinwen:
#
#         title=n.get_text()
#         link=n.get("href")
#         data={'标题': title.encode('utf-8'), '链接': link.encode('utf-8')}
#         outputfile.write('标题:{} 链接：{}\n'.format(data['标题'],data['链接']))




# import urllib,urllib2
# import requests
# from bs4 import BeautifulSoup
# junshi_url="http://mil.qq.com/mil_index.htm"
# proxy = urllib2.ProxyHandler({'https': '47.91.78.201:3128'})
# opener = urllib2.build_opener(proxy)
# opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30')]
# urllib2.install_opener(opener)
# with open('tengxunjunshi2.txt','w') as outputfile:
#    web_page=requests.get(junshi_url).text
#    soup=BeautifulSoup (web_page,'html.parser')
#    junshixinwen=soup.find_all(class_='linkto')
#    for n in junshixinwen:
#         title=n.get_text()
#         data={'标题': title}
#         print type(title)
#         outputfile.write('{}\n'.format(data['标题']))


# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import re
import time
import datetime
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


class get_messages():           # 得到用户所有信息的类
    def __init__(self):
        self.login_url = 'https://vpn.fosu.edu.cn:8080/default2.aspx'
        self.vpn_url = 'https://vpn.fosu.edu.cn/por/login_psw.csp'
        self.user_inf_url = "https://vpn.fosu.edu.cn:8080/xstop.aspx"          # 得到学生信息
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"}
        self.session = requests.Session()
        self.svpn_name = '20150390109'
        self.svpn_password = 'xsj510211...'
        self.user = ''
        self.pw = ''

    def login_vpn(self):
        vpn_data = {
            "mitm_result": '',
            "svpn_name": self.svpn_name,
            "svpn_password": self.svpn_password,
            }
        self.session.post(self.vpn_url, data=vpn_data, headers=self.headers, verify=False)

    def post_student_massage(self):
        r = self.session.get(self.login_url, verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')           # 使用bs获取viewstate
        text = soup.find('form').find('input', type="hidden")
        rb = u"学生".encode('gb2312', 'replace')             # 构建上传数据
        bu = u"登录".encode('gb2312', 'replace')
        data = {
            "__VIEWSTATE": text['value'],
            "yh": self.user,
            "kl": self.pw,
            "RadioButtonList1": rb,
            "Button1": bu,
            "CheckBox1": "on"
            }
        self.session.post(self.login_url, data=data, headers=self.headers, verify=False)
        return self.session

    def check_is_login(self,user,pw):
        self.user = user     # 保存数据于self
        self.pw = pw
        self.login_vpn()      # 登陆vpn
        s = self.post_student_massage()
        cj_url = "https://vpn.fosu.edu.cn:8080/xscj.aspx?xh="+self.user
        r_cj = s.get(cj_url, headers=self.headers, verify=False)
        if r_cj.text == "<script languange='javascript'>window.parent.location='';</script>":
            return False        # 密码或账号错误时进行提示
        else:
            return True

    def get_student_grade(self):     # 进行登录的函数，爬取信息的函数
        cj_url = "https://vpn.fosu.edu.cn:8080/xscj.aspx?xh="+self.user
        r_cj = self.session.get(cj_url, headers=self.headers, verify=False)
        all_terms = [
            {"y": "2017-2018", "t": "2"},
            {"y": "2017-2018", "t": "1"},
            {"y": "2016-2017", "t": "2"},
            {"y": "2016-2017", "t": "1"},
            {"y": "2015-2016", "t": "2"},
            {"y": "2015-2016", "t": "1"},
            {"y": "2014-2015", "t": "2"},
            {"y": "2014-2015", "t": "1"}, ]
        grade_list = []
        pattern1 = '<span id="jqpjf">全部学期学分积\(必修,限选,毕业论文\)为：(.*?)。\(公式：学分乘以最高分数的和除以学分的和\)</span>'
        xuefenji = re.findall(pattern1, str(r_cj.text))
        # print xuefenji[0]
        choice = 0
        for term in all_terms:

            pattern = "<td>"+term['y']+"</td><td>"+term['t']+"</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>&(.*?);</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?);</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>"
            m_tr = re.findall(pattern, r_cj.text)
            m_tr = m_tr[0:]
            if not m_tr:
                continue
            else:
                choice = choice+1
            t = dict()
            t['term'] = term['y']+"第"+term['t']+"学期"
            if choice == 1:
                t['flag'] = 'active'
            else:
                t['flag'] = ''
            t['lists'] =[]
            for line in m_tr:
                line = list(line)
                # print len(line)
                for i in range(len(line)):
                    if line[i] == '&nbsp;':
                        line[i] = '-'
                s = {'km': line[0], 'ps_cj': line[4], 'sy_cj': line[6], 'qm_cj': line[7], 'zp_cj': line[8], 'xuefen': line[11]}
                t['lists'].append(s)
            grade_list.append(t)
            # print grade_list
        return grade_list, xuefenji[0]

    def get_student_information(self):
        r_cj = self.session.get(self.user_inf_url, headers=self.headers, verify=False)
        xm = r'<span id="lbXM">(.*?)</span>'
        zy = r'<span id="lbBJMC">(.*?)</span>'
        xh = r'<span id="lbXH">(.*?)</span>'
        xm = re.findall(xm, r_cj.text)
        zy = re.findall(zy, r_cj.text)
        xh = re.findall(xh, r_cj.text)
        user_information = {
            'xm': xm[0],
            'zy': zy[0],
            'xh': xh[0],
        }
        with open('test.txt', 'a+') as f:
            f.write(xm[0]+','+zy[0]+','+xh[0]+','+str(datetime.datetime.now())+'\n')
        return user_information


fosu100net = get_messages()

# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import re
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


class get_messages():           # 得到用户所有信息的类
    def __init__(self):
        self.login_url = 'https://vpn.fosu.edu.cn:8080/default2.aspx'
        self.vpn_url = 'https://vpn.fosu.edu.cn/por/login_psw.csp'
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"}
        self.s = requests.Session()

    def login_vpn(self):
        svpn_name = '20150390109'
        svpn_password = 'xsj510211...'
        vpn_data = {
            "mitm_result": '',
            "svpn_name": svpn_name,
            "svpn_password": svpn_password,
            }
        self.s.post(self.vpn_url, data=vpn_data, headers=self.headers, verify=False)

    def post_student_massage(self, user, pw):
        r = self.s.get(self.login_url, verify=False)
        # 使用bs获取viewstate
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.find('form').find('input', type="hidden")
        # 构建上传数据
        rb = u"学生".encode('gb2312', 'replace')
        bu = u"登录".encode('gb2312', 'replace')
        data = {
            "__VIEWSTATE": text['value'],
            "yh": user,
            "kl": pw,
            "RadioButtonList1": rb,
            "Button1": bu,
            "CheckBox1": "on"
            }
        self.s.post(self.login_url, data=data, headers=self.headers, verify=False)
        return self.s

    def check_is_login(self,user,pw):
        # try:
            self.login_vpn()      # 登陆vpn
            s = self.post_student_massage(user, pw)
            cj_url = "https://vpn.fosu.edu.cn:8080/xscj.aspx?xh="+user
            headers = {
                'Referer': "https://vpn.fosu.edu.cn:8080/xsleft.aspx?flag=xxcx",
                'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36"
                }
            r_cj = s.get(cj_url, headers=headers, verify=False)
            if r_cj.text == "<script languange='javascript'>window.parent.location='';</script>":
                return False
            else:
                return True


    def get_student_grade(self, user, pw):     # 进行登录的函数，爬取信息的函数
        s = self.post_student_massage(user, pw)
        cj_url = "https://vpn.fosu.edu.cn:8080/xscj.aspx?xh="+user
        headers = {
            'Referer': "https://vpn.fosu.edu.cn:8080/xsleft.aspx?flag=xxcx",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36"
            }
        r_cj = s.get(cj_url, headers=headers, verify=False)
        if r_cj.text == "<script languange='javascript'>window.parent.location='';</script>":
            return False                      # 密码或账号错误时进行提示
        choice = [
            {"a": "2016-2017", "b": "2"},
            {"a": "2016-2017", "b": "1"},
            {"a": "2015-2016", "b": "2"},
            {"a": "2015-2016", "b": "1"},
            {"a": "2014-2015", "b": "2"},
            {"a": "2014-2015", "b": "1"}, ]
        grade_list = []
        pattern1 = '<span id="jqpjf">全部学期学分积\(必修,限选,毕业论文\)为：(.*?)。\(公式：学分乘以最高分数的和除以学分的和\)</span>'
        xuefenji = re.findall(pattern1, str(r_cj.text))
        # print xuefenji[0]
        for i in choice:
            pattern = "<td>"+i['a']+"</td><td>"+i['b']+"</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>&(.*?);</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?);</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>"
            m_tr = re.findall(pattern, r_cj.text)
            m_tr = m_tr[0:]
            if not m_tr:
                break
            t = dict()
            t['term'] = i['a']+"第"+i['b']+"学期"
            if i['a'] == '2016-2017' and i['b'] == '2':
                t['flag'] = 'active'
            else:
                t['flag'] = ''
            t['lists'] =[]
            for line in m_tr:
                line = list(line)
                s = {'km': line[0],'ps_cj': line[4],'sy_cj': line[6],'qm_cj': line[7], 'zp_cj': line[8],'xuefen': line[11]}
                t['lists'].append(s)
            grade_list.append(t)
            # print grade_list
        return grade_list, xuefenji[0]

    def get_student_information(self, user, pw):
        s = self.post_student_massage(user, pw)
        user_inf_url = "https://vpn.fosu.edu.cn:8080/xstop.aspx"          # 得到学生信息
        headers = {
            'Referer' : "https://vpn.fosu.edu.cn:8080/xsmainfs.aspx?xh="+user,
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36"
            }
        r_cj = s.get(user_inf_url, headers=headers, verify=False)
        # print r_cj.text
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
        return user_information


fosu100net = get_messages()



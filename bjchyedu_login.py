'''
注销信息
http://rz.bjchyedu.cn:801/eportal/?c=Portal&a=login&callback=dr1657497322305&login_method=1&user_account=15652627396&user_password=123456&wlan_user_ip=58.116.49.88&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.1&_=1657497287544
=
作者：hifuer
版本：1.0
联系方式：hifuer@qq.com
功能：朝阳网认证自动化认证
使用环境：安装 并配置好 python3.7  和requests 库  环境

使用方法：修改 name :手机号   password: 密码  ip:要上网主机IP地址 3个参数
    
    name='xxxxxxxxxxxx'  
    password='xxxxxx'
    ip='xx.xxx.xx.xx'

方法1：cmd 下
python login.py

简单的方法：配置好login.py 默认 python打开   并添加到开始启动项  
'''
import requests
name='您的手机号'
password='123456'
ip='您的IP地址'
#urls 有三个地址:分别是注销，登录，测试
def login(name,password,ip):
	urls=['http://rz.bjchyedu.cn:801/eportal/?c=Portal&a=login&callback=dr1657497322305&login_method=1&user_account={}&user_password={}&wlan_user_ip={}'.format(name,password,ip),'https://hao.360.com/?src=lm&ls=n792a71ec92']

	header={
	    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	}
	#认证
	try:
	    for url in urls:
	        r=requests.get(url,headers=header)
	    #print(r.text[361:706])  #测试语句
	except:
	    pass

login(name,password,ip)

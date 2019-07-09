import os

# 服务相关配置
# API_URL = 'https://api-qa.weizhilian.com'
API_URL = 'http://app-api-qa.weizhilian.com'
APP_SELECT = 'UHMnbNFdB3eNEOc6CxmcRUXU3GbsUMhB0eIgTERlS4FMUs9DytYOAzuEI8P7jlkRPhtG1Vwh'

API_HEADER = {
	# "content-type": "application/x-www-form-urlencoded",
	"aid": "174",
	"bid": "10006",
	"sid": "181",
	"uid": "131",
	"token": "36d8015fbf3949ddd53234b5669d248b",  # token指定用户并直接修改过期时间
	"locale": "zh-CN",
	"lon": "",
	"Accept": "*/*",
	"sdkVersion": "2.7.2",
	"Accept-Language": "zh-cn",
	"lat": "",
	"language": "zh-CN",
	"miniVersion": "2.3.2.10006",
	"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN",
	"Referer": "https://servicewechat.com/wxd9a28df0646534d8/0/page-frame.html",
	"Content-Length": "436",
	"Accept-Encoding": "br, gzip, deflate",
	"Connection": "keep-alive",
	}

# 设置目录的绝对路径;__file__当前文件绝对路径
BASE_PATH = os.path.dirname(
		os.path.abspath(__file__)
		)
print(BASE_PATH)

# yaml测试用例存放位置,拼接绝对路径
DATA_PATH = os.path.join(BASE_PATH, 'data')
CASE_PATH = os.path.join(BASE_PATH, 'cases')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
LIB_PATH = os.path.join(BASE_PATH, 'lib')

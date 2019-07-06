import os

# 服务相关配置
API_URL = 'https://api-qa.weizhilian.com'
# APP_KEY = '4AB1B9B72E44971F709011A0FFE68680'
APP_SELECT = 'UHMnbNFdB3eNEOc6CxmcRUXU3GbsUMhB0eIgTERlS4FMUs9DytYOAzuEI8P7jlkRPhtG1Vwh'

API_HEADER = {
	"content-type": "application/json",
	"bid": "10006",
	"sid": "96",
	"uid": "30",
	"token": "066e9487bcf12e58af1662a18e738c90",  # token指定用户并直接修改过期时间
	"locale": "zh-CN",
	"lon": "104.05883026123047",
	"Accept": "*/*",
	"sdkVersion": "2.7.2",
	"Accept-Language": "zh-cn",
	"lat": "30.548831939697266",
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

import unittest
import os, sys
import time

# 把项目目录加入环境变量，保证代码在任何地方运行都能成功
OBJ_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(OBJ_PATH)

from BeautifulReport import BeautifulReport as BR
from lib.utils import *

generate_test_file()
discover = unittest.defaultTestLoader.discover(
		start_dir = CASE_PATH,
		pattern = '*.py'
		)

month = time.strftime('%Y%m')
now = time.strftime('%Y%m%d%H%M%S')
html_name = now
runner = BR(discover)
runner.report(
		description = '划菜端接口自动化测试报告',
		filename = now,
		log_path = REPORT_PATH,
		)

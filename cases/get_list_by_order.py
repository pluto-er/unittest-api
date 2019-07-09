import unittest
from lib.utils import *
from setting import *
import ddt

@ddt.ddt
class Get_list_by_order(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.responses = {}

    @ddt.file_data(os.path.join(DATA_PATH,'get_list_by_order.yaml'))
    def test_get_list_by_order( self,**params):
        self._testClassName = params.get('case')  # 测试类
        self._testMethodName = params.get("uri")  # 请求方法
        self._testMethodDoc = params.get('detail')  # 用例说明
        url = API_URL + params.get('uri')
        method = params.get('method')
        data = params.get('data')
        check = params.get('check')
        header = API_HEADER  # 获取头部数据

        # 依赖数据获取
        rely_data = params.get("rely")
        if rely_data:
            data = rely_func(rely_data)
            if not data:
                return
        # 根据方法构造请求
        if method.lower() == 'post':
            res = requests.post(url, json = data, headers = header)
        else:
            res = requests.post(url, params = data, headers = header)
        resp = res.json()

        # 打印数据
        print("请求数据：", data, "<br/>")
        print("HOST：", url, "<br/>")
        print("Header", header)
        print("status：", resp['status'])
        print("Message：", resp['message'])
        print("响应结果：", resp)
        print("断言内容：", check)

        # 断言
        for c in check:
            self.assertIn(c, set_res_data(res.text))

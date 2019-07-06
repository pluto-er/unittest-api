import hashlib
import json
import re
from jsonpath_rw import parse
from setting import *

#加密为MD5码
def get_md5(pwd):
    md5 = hashlib.md5()
    md5.update(str(pwd).encode('utf-8'))
    return md5.hexdigest()
    # return md5.hexdigest().upper()
#得到签名
def set_sign(params,key=None,secret=None):
    # secrect = "UHMnbNFdB3eNEOc6CxmcRUXU3GbsUMhB0eIgTERlS4FMUs9DytYOAzuEI8P7jlkRPhtG1Vwh"
    if not params:
        params={}
    key = key
    secret = secret or APP_SELECT
    params.pop('app_secret',None)
    # params['app_key'] = key
    s = ""
    li = list(params.keys())
    li.sort()
    # print(li)
    for i in li:
        s += str(params[i])
        # print(i)
    s = s + secret    #使用MD5加密传输密码
    params['sign'] = get_md5(s).upper()
    return params
    # return get_md5(s)
#返回的报文是json格式的，利用字符替换让数据变成“a=1，b=2”的格式
def set_res_data(res):
    if res:
        return  res.lower().replace('":"','=').replace('":','=')

def generate_test_file():
    """
    根据data目录中的yaml用例文件，自动生成cases目录下的py文件
    :return:
    """
    yaml_file = os.listdir(DATA_PATH)
    print(yaml_file)

    for file in yaml_file:
        if file.endswith('yaml') or file.endswith('yml'):
            method_name = file.replace('.yaml','').replace('.yml','')
            file_name = file
            class_name = method_name.capitalize()
            with open(os.path.join(BASE_PATH,'base.text'),encoding = 'utf-8') as f:
                content = f.read() % {
                    "class_name":class_name,
                    "file_name":file_name,
                    "method_name":method_name
                }
            py_file_name = os.path.join(CASE_PATH,method_name + '.py')
            with open(py_file_name,'w',encoding='utf-8') as py:
                py.write(content)

def deal_with_rely(data,resps):
    #把data转换成字符串
    data = json.dumps(data)
    # print("data字典：",data)
    #用正则表达式去匹配
    pattern = re.compile(r'\$\{(.+?)\}')
    #找到的结果是login:data.uuid
    params = pattern.findall(data)
    # print("params:",params)
    for p in params:
        #把login:data.uuid分开
        case_id,path = p.split(":")
        # print("Case_id:",case_id," Path:",path)
        # resp = json.loads(resps[case_id])
        resp = resps[case_id]
        # print(type(resp))
        # print("resp:",resp)
        # resp = json.dumps(resp)
        #用data.uuid到reps中去取对应的内容
        json_exe = parse(path)
        # print("json_exe:",json_exe)
        # resp = json.loads(resp)
        value = [match.value for match in json_exe.find(resp)][0]
        for match in json_exe.find(resp):
            value = match.value
            print(value)
    #     print("value:",value)
    #     #用正则表达式替换匹配到的内容，也就是${login:data.uuid}，替换成实际的值
    #     data = pattern.sub(value,data,1)
    #     print(data)
    # #将data转回字典
    # data = json.loads(data)
    # return data

if __name__ == '__main__':
    data = {
        's': 'App.User.Profile',
        'app_key': 'AB1B9B72E44971F709011A0FFE68680',
        'uuid': '${login: data.uuid}',
        'token':'${login: data.token}'
    }
    resps ={'login':{'ret': 200,'data':
                {
                    'err_code': 0,
                    'err_msg': '',
                    'uuid': '969F073C0118451DD26E9151D1BEA72A',
                    'token': '9715C4D4C306522C94F76FABA11B7D7E04B1AF25F66ECBD535D49412B49FA98E'},
                'msg': '当前请求接口：App.User.Login'}
            }
    print(deal_with_rely(data, resps))
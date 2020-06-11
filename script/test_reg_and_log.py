# 导包
import requests
import unittest

from parameterized import parameterized

from api.register_api import RegisterApi
from app import BASE_DIR
from utils import assert_common, load_data


# 定义测试类


class TestRegAndLog(unittest.TestCase):
    # 定义初始化类
    @classmethod
    def setUpClass(cls):
        cls.reg_api = RegisterApi()

    # 定义初始化方法
    def setUp(self):
        # 实例化session
        self.session = requests.Session()

    # 定义销毁方法
    def tearDown(self):
        # 关闭session
        if self.session:
            self.session.close()

    @parameterized.expand(load_data(BASE_DIR + "/data/reg_and_log_data.json"))
    # 定义注册方法
    def test01_reg(self, request_body, http_code, status, reg_msg, log_msg):
        # 获取验证码令牌
        self.reg_api.get_reg_ver(self.session)
        # 使用令牌的注册
        response_reg = self.reg_api.register(self.session, data=request_body)
        print("注册的结果为：", response_reg.json())

        # 添加断言
        assert_common(self, http_code, status, reg_msg, response_reg)

    @parameterized.expand(load_data(BASE_DIR + "/data/reg_and_log_data.json"))
    # 定义登录方法
    def test02_log(self, request_body, http_code, status, reg_msg, log_msg):
        # 获取登录的验证码令牌
        self.reg_api.get_log_ver(self.session)
        # 获取登录的接口
        response_log = self.reg_api.login(self.session, data=request_body)
        print("登录的结果为：", response_log.json())

        # 添加断言
        assert_common(self, http_code, status, log_msg, response_log)

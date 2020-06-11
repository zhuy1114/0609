# 导包
import time
import unittest
from BeautifulReport import BeautifulReport
from app import BASE_DIR

# 组织测试用例
suite = unittest.TestLoader().discover(BASE_DIR + "/script", pattern="test*.py")

# 生成报告名字
file_name = "/report-{}.html".format(time.strftime("%Y%m%d%H%M%S"))

# 执行报告
BeautifulReport(suite).report(filename=file_name, description="By_myself ->tpshop注册登录引用参数化",
                              log_path=BASE_DIR + "/report")

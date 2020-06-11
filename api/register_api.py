# 定义类
class RegisterApi:
    def __init__(self):
        # 注册的获取验证码
        self.reg_ver_url = "http://localhost/index.php/Home/User/verify/type/user_reg.html"
        # 注册接口
        self.register_url = "http://localhost/index.php/Home/User/reg.html"
        # 登陆的获取验证码
        self.log_ver_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        # 登陆接口
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 获取注册页面验证码接口方法
    def get_reg_ver(self, session):
        return session.get(url=self.reg_ver_url)

    # 获取注册的接口方法
    def register(self, session, data):
        return session.post(url=self.register_url, data=data)

    # 获取登录验证码接口方法
    def get_log_ver(self, session):
        return session.get(url=self.log_ver_url)

    # 获取登录的接口方法
    def login(self, session, data):
        return session.post(url=self.login_url, data=data)

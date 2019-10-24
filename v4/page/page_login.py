from v4 import page
from v4.base.base import Base


class PageLogin(Base):
    # 关闭 弹窗
    def page_close_alert(self):
        self.base_click(page.login_close_alert)

    # 点击 我
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击 已有账号, 去登录
    def psge_click_username_exists(self):
        self.base_click(page.login_username_exists)

    # 输入 用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入 密码
    def page_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击 登录
    def page_click_dl(self):
        self.base_click(page.login_btn)

    # 组合业务方法
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_pwd(pwd)
        self.page_click_dl()


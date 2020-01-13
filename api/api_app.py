import time

import requests

import api
from tools.get_log import GetLog
from tools.read_txt import read_txt

log = GetLog.get_logger()


class ApiApp:

    # 初始化 组装url (服务器IP + 端口 + 资源path)
    def __init__(self):
        # 定义 登录url
        self.url_app_login = api.HOST + "/app/v1_0/authorizations"
        log.info("正在初始化APP登录url：{}".format(self.url_app_login))
        # 定义 手机端搜索文章的url
        self.url_app_search = api.HOST + "/app/v1_1/articles"
        log.info("正在初始化频道新闻推荐url：{}".format(self.url_app_search))

    def api_app_login(self):
        """
        app 登录的方法

        :return: 响应对象
        """
        login_data = read_txt("mp_login.txt")[0]
        data = {"mobile": login_data[0], "code": login_data[1]}
        # 调用post方法
        log.info("正在调用APP的登录的方法，手机号：{}验证码{}".format(login_data[0], login_data[1]))
        return requests.post(url=self.url_app_login, json=data, headers=api.headers)

    def api_app_search(self):
        """
        # 获取频道下的新闻 的方法

        :return: 响应对象
        """
        data = {"channel_id": 7,
                "timestamp": int(time.time()),
                "with_top": 1
                }
        log.info("正在调用APP搜索的方法，发布的数据是：{}请求头数据为：{}".format(data, api.headers))
        # 调用get方法
        return requests.get(url=self.url_app_search, params=data, headers=api.headers)

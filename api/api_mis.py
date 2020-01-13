import requests

import api
from api import HOST
from tools.get_log import GetLog

log = GetLog.get_logger()


class ApiMis:

    def __init__(self):
        """
        初始化
        """
        # 登录url
        self.url_mis_login = HOST + "/mis/v1_0/authorizations"
        log.info("正在初始化管理员登录的url：{}".format(self.url_mis_login))

        # 查询url
        self.url_mis_search = HOST + "/mis/v1_0/articles"
        log.info("正在初始化查询的url：{}".format(self.url_mis_search))

        # 审核url
        self.url_mis_audit = HOST + "/mis/v1_0/articles"
        log.info("正在初始化审核的url：{}".format(self.url_mis_audit))

    def api_mis_login(self, account, pwd):
        """
        管理员登录成功  方法
        :param account:管理员账号
        :param pwd:管理员密码
        :return:响应对象
        """
        # 组合数据
        data = {"account": account, "password": pwd}
        log.info("管理员登录成功，数据为：{}请求信息头为：{}".format(data, api.headers))
        return requests.post(url=self.url_mis_login,
                             json=data,
                             headers=api.headers)

    def api_mis_search(self):
        """
         查询文章 方法
        :return:响应对象
        """
        data = {"title": api.title, "channel": api.channel}
        log.info("查询文章，数据为：{}请求信息头为：{}".format(data, api.headers))
        return requests.get(url=self.url_mis_search,
                            params=data,
                            headers=api.headers)

    def api_mis_audit(self):
        """
        审核文章 方法
        :return: 响应对象
        """
        data = {"article_ids": [api.article_id], "status": 2}  # 2为审核通过
        log.info("审核文章，数据为：{}请求信息头为：{}".format(data, api.headers))
        return requests.put(url=self.url_mis_audit,
                            json=data,
                            headers=api.headers)

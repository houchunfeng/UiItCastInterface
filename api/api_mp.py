import requests

import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class ApiMp:
    # 初始化 组装url (服务器IP + 端口 + 资源path)
    def __init__(self):
        # 定义 登录url
        self.url_mp_login = api.HOST + "/mp/v1_0/authorizations"
        log.info("正在初始化自媒体登录url：{}".format(self.url_mp_login))
        # 定义 发布文章url
        self.url_mp_article = api.HOST + "/mp/v1_0/articles"
        log.info("正在初始化发布文章url：{}".format(self.url_mp_article))

    def api_mp_login(self, mobile, code):
        """
        登录 接口封装方法
        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象
        """
        data = {"mobile": mobile, "code": code}
        # 调用post方法
        log.info("正在调用自媒体的登录的方法，手机号：{}验证码{}".format(mobile, code))
        return requests.post(url=self.url_mp_login, json=data, headers=api.headers)

    def api_mp_article(self, title, content, channel_id):
        """
        发布文章 接口封装方法
        :param title: 文章标题
        :param content: 文章内容
        :param channel_id: 文章所属频道7 为数据库
        :param cover: 封面  0为自动
        :return: 响应对象
        """
        data = {
            "title": title,
            "content": content,
            "channel_id": channel_id,
            "cover": {"type": 0, "images": []}
        }
        log.info("正在调用自媒体发布文章的方法，发布的数据是：{}请求头数据为：{}".format(data, api.headers))
        # 调用post方法
        return requests.post(url=self.url_mp_article, json=data, headers=api.headers)

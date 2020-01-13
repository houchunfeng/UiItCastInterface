import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class ToolsInter:

    @classmethod
    def get_token(cls, response):
        """
        提取token
        :param response: 响应的信息
        :return: 响应结果
        """
        # 提取token
        token = response.json().get("data").get("token")
        log.info("正在调用get_token()方法，取到的token是：{}".format(token))
        # 将提取的token追加到api.headers中，发布文章使用
        api.headers['Authorization'] = "Bearer " + token

    @classmethod
    def assert_common(cls, response, code=201, message="OK", ):
        """
        断言
        :param response: 响应信息
        :param code: 状态码
        :param message: 响应的具体信息
        :return: 响应结果
        """
        try:
            # 断言响应信息message

            assert message == response.json().get("message")
            # 断言状态码
            assert code == response.status_code
        except Exception as e:
            log.error(e)
            raise

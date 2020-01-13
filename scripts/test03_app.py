from api.api_app import ApiApp
from tools.tools_inter import ToolsInter


class TestApp:

    def setup_class(self):
        """
        初始化
        :return:
        """
        # 获取ApiApp对象
        self.app = ApiApp()

    def test01_app_login(self):
        """
        app登录测试用例
        :return:
        """
        # 调用登录接口
        r = self.app.api_app_login()
        # 提取token
        ToolsInter.get_token(r)
        # 断言
        ToolsInter.assert_common(r)

    # 查询文章
    def test02_app_search(self):
        """
        app查询文章的测试用例
        :return:
        """

        # 调用查询接口
        r = self.app.api_app_search()
        # 断言
        ToolsInter.assert_common(r, code=200)

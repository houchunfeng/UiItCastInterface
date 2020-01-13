import pytest

from api.api_mis import ApiMis
from tools.read_txt import read_txt
from tools.tools_inter import ToolsInter


class TestMis:

    def setup_class(self):
        """
        初始化
        :return:
        """
        # 获取ApiMis对象
        self.mis = ApiMis()

    @pytest.mark.parametrize("account, pwd", read_txt("mis_login.txt"))
    def test01_mis_login(self, account, pwd):
        """
        管理员 登录测试方法
        :param account: 管理员账号
        :param pwd: 密码
        :return:
        """
        # 调用登录接口方法
        rep = self.mis.api_mis_login(account, pwd)
        # 提取token
        ToolsInter.get_token(rep)
        # 断言
        print(rep.json())
        ToolsInter.assert_common(rep)

    def test02_mis_search(self):
        """
        查询文章测试用例
        :return:
        """
        # 调用查询接口方法
        rep = self.mis.api_mis_search()
        # 断言

        ToolsInter.assert_common(rep, code=200)

    def test03_mis_audit(self):
        """
        审核文章测试用例
        :return:
        """
        # 调用审核接口 方法
        rep = self.mis.api_mis_audit()
        # 断言
        ToolsInter.assert_common(rep)

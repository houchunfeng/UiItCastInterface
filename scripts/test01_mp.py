import pytest

import api
from api.api_mp import ApiMp
from tools.read_txt import read_txt
from tools.tools_inter import ToolsInter


class TestMp:
    # 初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.mp = ApiMp()

    @pytest.mark.parametrize("mobile,code", read_txt("mp_login.txt"))
    def test01_mp_login(self, mobile, code):
        """
        登录测试方法
        :param mobile: 手机号
        :param code: 验证码
        :return:
        """
        # 调用登录接口方法
        r = self.mp.api_mp_login(mobile, code)
        # 提取token
        ToolsInter.get_token(r)
        # 断言
        print(r.json())
        ToolsInter.assert_common(r)

    #
    @pytest.mark.parametrize("title, content, channel_id,channel_name", read_txt("mp_article.txt"))
    def test02_mp_article(self, title, content, channel_id, channel_name):
        """
        发布文章测试用例
        :param title: 文章标题
        :param content: 文章内容
        :param channel_id:
        :param channel_name:
        :return:
        """
        # 调用发布文章接口方法
        r = self.mp.api_mp_article(title, content, channel_id)
        # 发布文章成功id，生成文章id---审核文章使用
        api.article_id = r.json().get("data").get("id")
        # 断言
        ToolsInter.assert_common(r)

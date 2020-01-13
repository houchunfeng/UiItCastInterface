from tools.read_txt import read_txt

"""公共url定义"""
HOST = "http://ttapi.research.itcast.cn"
"""公共headers"""
headers = {"Content-Type": "application/json"}
# 发布文章id
article_id = None
# 文章title
title = read_txt("mp_article.txt")[0][0]
# 频道id
channel_id = read_txt("mp_article.txt")[0][2]
# 文章频道 id为7 的频道为数据库
channel = read_txt("mp_article.txt")[0][3]

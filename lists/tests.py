from django.urls import resolve
from django.test import TestCase
#接下来需要定义的视图函数，作用是返回所需的HTML。从import语句可以看出，要把这个函数保存到文件 lists/views.py
from lists.views import home_page
from django.http import HttpRequest
from django.http import HttpResponse


# Create your tests here.
#
#resolve是Django内部使用的函数，用于解析URL，并将其映射到相应的视图函数上。
#检查解析网站根路径“/”时，是否能找到名为home_page 的函数
#  def test_bad_maths(self):
#  self.assertEqual(1+1,3)
#

class HomePageTest(TestCase):
  def test_root_url_resolves_to_home_page_view(self):
      found = resolve('/')
      self.assertEqual(found.func,home_page)

#1. 创建一个HttpRequest对象，用户在浏览器中请求网页时，Django看到的就是HttpRequest对象
#2. 把这个HttpRequest对象传送给Home_Page视图，得到响应。
#    断定响应的.content属性，（即发送给用户的HTML）中有特定的内容。
#3. 希望相应<html>标签开头，并在结尾处关闭该标签。注意，response.content是原始字节，不是python字符串，因此对比是要使用b''句法。
# 4. 希望响应中有一个<title>标签，其内容包含单词”To-Do“---因为在功能测试中做了这项测试

  def test_home_page_returns_correct_html(self):
      request = HttpRequest()
      response = home_page(request)
      self.assertTrue(response.content.startswith(b'<html>'))
      self.assertIn(b'<title>To-Do lists</title>', response.content)
      self.assertTrue(response.content.endswith(b'</html>'))

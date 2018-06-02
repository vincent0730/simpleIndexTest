from django.urls import resolve
from django.test import TestCase
#接下来需要定义的视图函数，作用是返回所需的HTML。从import语句可以看出，要把这个函数保存到文件 lists/views.py
from lists.views import home_page



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


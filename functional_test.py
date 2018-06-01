#启动一个Selenium webdriver,打开一个真正的firefox浏览器窗口
from selenium import webdriver
import unittest

#测试组织成类的形式，继承自unittest.TestCase
class NewVisitorTest(unittest.TestCase):

    #
    #1. setUp和tearDown是特殊的方法，分别在各个测试方法之前和之后运行。我使用这两个方法打开和关闭浏览器。
    #   这两个方法和try/except类似，就算测试中出错了，也会运行tearDown方法。测试结束后，Firefox窗口不会一直停留在桌面上
	#2. implicitly_wait是隐式等待，在selenium操作之前等待页面完成加载，在简单的应用中可以使用，但是当应用超过某种复杂度之后，则需要显式等待规则
    #
    def setUp(self):
        self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    #
    #1. 测试的主要代码写在此方法中，名字以test_开头的方法都是测试方法，由测试运行程序运行。
    #     类中可以定义多个测试方法。为测试方法起个有意义的名字是至关重要的。
    #2. 使用self.assertIn代替assert编写测试断言。unittest提供了很多这种用于编写测试断言的辅助函数。如assertEqual、assertTrue、assertFalse等。
    #3. self.fai生成指定的错误消息，在这里使用这个方法提醒测试结束了
    #
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        
        self.assertIn('To-Do',self.browser.titile)

        self.fail('Finish the test!')

#
#python是使用这个语句检查自己是否在命令中运行，而不是在其他脚本中导入
#调用unittest.main()启动unittest的测试运行程序，这个程序会在文件中自动查找测试类和方法，然后运行。
#warnings='ignore'的作用是禁止抛出ResourceWearing异常。
#
if _name_ == '_main_':
     unittest.main(warnings='ignore')  





#browser = webdriver.Firefox()

#在浏览器打开我们期望本地电脑伺服的网页
#browser.get('http://localhost:8000')

#检查（做一个测试断言）这个我那个网页的中是否包含了单词‘Django’
#assert 'Django'in browser.title

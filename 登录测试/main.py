from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread

class test(Thread):
    pattern=""
    file=""
    def run(self) -> None:
        tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern=self.pattern)

        runner = HTMLTestRunner.HTMLTestRunner(
            title = "HKR系统测试报告",
            description= "HKR系统登陆测试",
            verbosity=1,
            stream = open(file=self.file,mode="w+",encoding="utf-8")
)

        runner.run(tests)

# 邮件发送模块

r1=test()
r1.pattern="TestLogin.py"
r1.file="登录成功.html"
r1.start()


r2=test()
r2.pattern="loginError.py"
r2.file="账户名错误或密码错误.html"
r2.start()



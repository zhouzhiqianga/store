
'''
    任务1：
        使用多线程同步执行用例。
    任务2:
        修改头像的脚本写一份。
'''
class LoginOperation:

    def __init__(self,driver):
        self.driver = driver

    def login(self,username,pwd):
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()


    def getSuccess_result(self):
        return self.driver.title


    def getError_result(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text
















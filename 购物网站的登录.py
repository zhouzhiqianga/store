from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


#京东登录
# driver=webdriver.Chrome()
# driver.get("https://passport.jd.com")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@class='link-login']").click()
# time.sleep(2)
# data = driver.window_handles
# driver.switch_to.window(data[0])
# driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='loginname']").send_keys("13072033978")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("zhou23688165.")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
#
# a = ActionChains(driver)
# b = driver.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")
# time.sleep(2)
# a.click_and_hold(b).move_by_offset(80,0).perform()
#
# a.release()



#b站登录
# driver=webdriver.Chrome()
# driver.get("https://www.bilibili.com")
# driver.find_element_by_xpath("//*[@id='internationalHeader']/div[1]/div/div[3]/div[2]/span[1]/div/span/div").click()
# time.sleep(2)
# data = driver.window_handles
# driver.switch_to.window(data[1])
# driver.find_element_by_xpath("//*[@id='login-username']").send_keys("13072033978")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='login-passwd']").send_keys("zhou23688165")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='geetest-wrap']/div/div[5]/a[1]").click()
#
# time.sleep(2)
# data = driver.window_handles
# driver.switch_to.window(data[1])
# driver.find_element_by_xpath("//*[@id='primaryChannelMenu']/span[10]/div/a/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='high_energy']/div[1]/div[2]/div[2]/a/div/div[3]").click()
# time.sleep(2)

# driver.find_element_by_xpath("//*[@id='bilibiliPlayer']/div[1]/div[1]/div[11]/div[2]/div[2]/div[1]/div[1]/button/span").click()


#知乎登录
driver=webdriver.Chrome()
driver.get("https://www.zhihu.com")
driver.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/span[2]/button[2]").click()
time.sleep(3)
#driver.find_element_by_xpath("//*[@id="root"]/div/main/div/div/div/div[3]/span[2]/button[2]")




























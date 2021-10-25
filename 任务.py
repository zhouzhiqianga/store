from selenium import webdriver
import time

#京东
driver = webdriver.Chrome()
driver.get("https://www.jd.com")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='key']").send_keys("华为手机")
time.sleep(3)
a=driver.current_window_handle
driver.find_element_by_xpath("//*[@class='button']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@class='gl-i-wrap']").click()
time.sleep(3)
for i in driver.window_handles:
    if i != a:
        driver.switch_to.window(i)
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()


#苏宁易购
# driver = webdriver.Chrome()
# driver.get("https://www.suning.com")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("华为手机")
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
# time.sleep(3)
# a=driver.current_window_handle
# driver.find_element_by_xpath("//*[@class='ltrbl']").click()
# time.sleep(3)
# for i in driver.window_handles:
#     if i != a:
#         driver.switch_to.window(i)
# driver.find_element_by_xpath("//*[@id='addCart']").click()







from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')

# 搜索框
browser.find_element_by_id('kw').send_keys('python')

# 点击按钮

browser.find_element_by_id('su').click()
print(browser.current_url)
time.sleep(6)

browser.get("http://www.douban.com")
browser.save_screenshot('douban.png')
time.sleep(2)
browser.back()
browser.forward()

browser.quit()

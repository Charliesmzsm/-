from selenium import webdriver

url = 'https://qzone.qq.com'
# url = 'https://www.baidu.com '

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=opt)


driver.get(url)
driver.save_screenshot('test.png')

# driver.switch_to.frame('login_frame')
#
# driver.find_element_by_id('switcher_plogin').click()
# driver.find_element_by_id('u').send_keys('1944930902')
# driver.find_element_by_id('p').send_keys('shiming143301003')
# driver.find_element_by_id('login_button').click()
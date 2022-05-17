from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait




# js学习

driver = webdriver.Chrome()
# 最大化
driver.maximize_window()
driver.implicitly_wait(10)


# 打开浏览器
# driver.get("http://prodplus.okaygis.com:8880/#/login")
# password = driver.find_element(By.XPATH, "//label[contains(text(), '密码')]/following-sibling::div/div/input")
# 改变某个属性的值
# js = """
# var pass = arguments[0];
# pass.type = 'text'
# pass.value = 123456
# return [pass.value]
# """
# driver.execute_script(js, password)


# driver.get("https://www.baidu.com/")
# driver.find_element(By.XPATH, "//*[@id='kw']").send_keys("微博")
# sleep(1)
# driver.find_element(By.XPATH, "//*[@id='su']").click()
# sleep(2)
# weibo = driver.find_element(By.XPATH, "//*[@id='1']/div/div[1]/h3/a[1]")
# 删除某个属性
# js = """
# var weibo = arguments[0];
# weibo.removeAttribute('target')
# return [weibo.value]
# """
# driver.execute_script(js, weibo)
# 拖动滚动条
# driver.execute_script("window.scrollTo(0,500)")
# weibo.click()

driver.get("http://prodplus.okaygis.com:8880/#/login")
driver.find_element(By.XPATH, "//label[contains(text(), '登录名')]/following-sibling::div/div/input").send_keys("shuirr")
driver.find_element(By.XPATH, "//label[contains(text(), '密码')]/following-sibling::div/div/input").send_keys("ok111111")
driver.find_element(By.XPATH, "//span[contains(text(), '登录')]").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '藏品管理')]").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '征集管理')]").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '线索录入')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '已指派')]").click()
# sleep(2)
# driver.find_element(By.XPATH, "//input[@placeholder='线索名称']").send_keys("日志填写")
# sleep(2)
# driver.find_element(By.XPATH, "//span[contains(text(), '查询')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '已废弃')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)


driver.find_element(By.XPATH, "//span[contains(text(), '线索跟踪')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '已完成')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '已终止')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)

driver.find_element(By.XPATH, "//span[contains(text(), '征集录入')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '已提交')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)

driver.find_element(By.XPATH, "//span[contains(text(), '征集中')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '已鉴定')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '已终止')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)

driver.find_element(By.XPATH, "//span[contains(text(), '确认征集')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '已征集')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)

driver.find_element(By.XPATH, "//span[contains(text(), '拨库管理')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), '已拨库')]").click()
sleep(2)
driver.find_element(By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
sleep(2)


# text = driver.find_element(By.XPATH, "(//label[contains(text(), '线索名称')]/following-sibling::div/div/input)[2]").text
# print(text)
# value = driver.find_element(By.XPATH, "(//label[contains(text(), '线索名称')]/following-sibling::div/div/input)[2]").get_attribute('value')
# print(value)

sleep(10)
driver.close()


# (//tr[contains(@class, 'el-table__row')])[1]/td[contains(@class, 'is-center')]/div/button/span[contains(text(), '编辑')]
# (//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span

# /html/body/div[1]/div/div[2]/div/div/div/div[4]/div/ div[3]         /table/tbody/tr/td[10]/div/button/span
# /html/body/div[1]/div/div[2]/div/div/div/div[4]/div/ div[4]/div[2]  /table/tbody/tr/td[10]/div/button/span
# /html/body/div/div/div[2]/div/div/div/div[4]/div/div[4]/div[2]/table/tbody/tr/td[10]/div/button/span
# (//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span
# ((//tbody)[2]//td[contains(@class, 'is-center')]//span)[1]
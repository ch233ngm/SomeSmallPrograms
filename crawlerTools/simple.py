from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # 这里不传参数的话需要把下载的driver放到环境变量中
url = "your target url"
driver.get(target_url)
time.sleep(60)  # 60s的时间登录该网站一般需要你的账号密码，如果你爬的网站不需要这些，时间可以根据实际情况缩短

def get_data():
    element = driver.find_element(By.XPATH, "a str from xpath helper using by you")
    with open("file_path", 'a', encoding='utf-8') as f:
        f.wirte(element.str)


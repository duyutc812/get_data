from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time


# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# firefox_capabilities['binary'] = '/usr/bin/firefox'
# browser = webdriver.Firefox(capabilities=firefox_capabilities)
browser = webdriver.Chrome()
browser.get("https://accounts.shopify.com/store-login")

store_address = browser.find_element_by_name('shop[domain]')
store_address.send_keys("duyutc812-1.myshopify.com")
btn_next = browser.find_element_by_name('commit')
btn_next.click()
time.sleep(1)

email = browser.find_element_by_name("account[email]")
email.send_keys("duyutc812@gmail.com")
time.sleep(1)
btn_next = browser.find_element_by_name('commit')
btn_next.click()
time.sleep(2)

password = browser.find_element_by_name("account[password]")
password.send_keys("fdwu2838FD")
time.sleep(3)
btn_next = browser.find_element_by_name('commit')
btn_next.click()
time.sleep(2)


cookies_list = browser.get_cookies()
jar = requests.cookies.RequestsCookieJar()

for cookie in cookies_list:
    jar.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'])
# print(jar)

time.sleep(5)
browser.close()

# type_datas = ['products', 'customers', 'orders']
type_datas = ['products']
for type_data in type_datas:
    url_path = "https://duyutc812-1.myshopify.com/admin/" + type_data + ".json"
    f = open((type_data + ".txt"), 'w')
    data = requests.get(url_path, headers={'User-agent': 'your bot 0.1'}, cookies=jar).json()
    # print(data)
    f.write(str(data))
    f.close()

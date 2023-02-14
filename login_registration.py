from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Registration_login: регистрация аккаунта

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")

driver.find_element_by_css_selector("#menu-item-50 > a").click()


email = "maks_ivanov_32@bk.ru"
password = "Babadu_322"

driver.find_element_by_id("reg_email").send_keys(email)
driver.find_element_by_id("reg_password").send_keys(password)
driver.find_element_by_name("register").click()

time.sleep(2)
driver.quit()

#Registration_login: логин в систему

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")

driver.find_element_by_css_selector("#menu-item-50 > a").click()


email = "maks_ivanov_32@bk.ru"
password = "Babadu_322"

time.sleep(4)

driver.find_element_by_id("username").send_keys(email)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("login").click()

time.sleep(4)

logout = driver.find_element_by_xpath("//*[text()='Logout']")
print(logout)
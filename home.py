from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 800);")

driver.find_element_by_css_selector(".col3-1.first.sub_column.sub_column_1-0-2-0.sub_column_post_22 h3").click()

driver.execute_script("window.scrollBy(0, 700);")

driver.find_element_by_css_selector(".reviews_tab > a").click()

driver.find_element_by_id("author").send_keys("Vlad")

driver.find_element_by_id("email").send_keys("maks_ivanov_32@bk.ru")

driver.find_element_by_id("submit").click()


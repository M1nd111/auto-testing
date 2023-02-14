from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Shop: отображение страницы товара

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")

driver.find_element_by_css_selector("#menu-item-40 > a").click()

driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']").click()



zagolovok = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "HTML5 Forms"))

if zagolovok == True: print("Заголовок книги HTML5 Forms корректный")

time.sleep(2)
driver.quit()

#Shop: количество товаров в категории

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")

driver.find_element_by_css_selector("#menu-item-40 > a").click()
time.sleep(2)
driver.find_element_by_css_selector(".cat-item.cat-item-19 > a").click()


item = driver.find_elements_by_css_selector(".product.type-product")

if len(item) == 3:
    print("Отображается 3 товара")
else:
    print("Ошибка! отображается ", item, " товара")

time.sleep(2)
driver.quit()

#Shop: сортировка товаров


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

time.sleep(2)

driver.find_element_by_css_selector("#menu-item-40 > a").click()

selector = driver.find_element_by_css_selector("[selected='selected']")
s_text = selector.text

if s_text == "Default sorting":
    print("Выбрана дефолтная сортировка")
else:
    print("выбрана сортировка:", s_text)

element = driver.find_element_by_css_selector("[name='orderby'].orderby")
sl = Select(element)
sl.select_by_visible_text("Sort by price: high to low")

selector = driver.find_element_by_css_selector("[selected='selected']")
s_text = selector.text

if s_text == "Sort by price: high to low":
    print("Выбрана верная сортировка")
else:
    print("выбрана сортировка:", s_text)

time.sleep(2)
driver.quit()

#Shop: отображение, скидка товара


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

time.sleep(2)

driver.find_element_by_css_selector("#menu-item-40 > a").click()

driver.find_element_by_css_selector("[title='Android Quick Start Guide']").click()

element = driver.find_element_by_css_selector(".price > del > span")
element_check = element.text
assert element_check == "₹600.00"

element2 = driver.find_element_by_css_selector(".price > ins > span")
element_check2 = element2.text
assert element_check2 == "₹450.00"

wait = WebDriverWait(driver,10)

img = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']")) )
img.click()

close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pp_close")))
close.click()

time.sleep(2)
driver.quit()

#Shop: проверка цены в корзине

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")

driver.find_element_by_css_selector("#menu-item-40 > a").click()

driver.execute_script("window.scrollBy(0, 500);")
driver.find_element_by_css_selector("[data-product_id='165']").click()
time.sleep(2)
driver.find_element_by_css_selector(".wpmenucart-contents > i").click()

PRICE = driver.find_element_by_css_selector("[data-title='Price'] .woocommerce-Price-amount.amount")
PRICE_check = PRICE.text

Subtotal = driver.find_element_by_css_selector("[data-title='Subtotal'] .woocommerce-Price-amount.amount")
Subtotal_check = Subtotal.text

wait = WebDriverWait(driver,10)

Sub = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal'] .woocommerce-Price-amount.amount"), PRICE_check) )
print("Subtotal", Sub)

Sub = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal'] .woocommerce-Price-amount.amount"), PRICE_check) )

TAX = driver.find_element_by_css_selector("[data-title='Tax'] .woocommerce-Price-amount.amount")
TAX_check = TAX.text
print(TAX_check)

TOTAL = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total [data-title='Total'] .woocommerce-Price-amount.amount"), "₹357.00"))
print("Total", TOTAL)

time.sleep(2)
driver.quit()

#Shop: работа в корзине

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")

driver.find_element_by_css_selector("#menu-item-40 > a").click()

driver.execute_script("window.scrollBy(0, 500);")

driver.find_element_by_css_selector("[data-product_id='165']").click()
time.sleep(2)
driver.find_element_by_css_selector(".wpmenucart-contents > i").click()

time.sleep(2)
driver.find_element_by_class_name("remove").click()

driver.find_element_by_css_selector(".woocommerce-message > a").click()

driver.find_element_by_css_selector(".input-text.qty.text").clear()
driver.find_element_by_css_selector(".input-text.qty.text").send_keys("3")

driver.find_element_by_name("update_cart").click()

quantity = driver.find_element_by_css_selector(".input-text.qty.text")

quantity_znach = quantity.get_attribute("value")

if quantity_znach == "3":
    print("quantity равен 3")
else:
    print("quantity равен:",quantity)

time.sleep(2)
driver.find_element_by_name("apply_coupon").click()

element = driver.find_element_by_css_selector(".woocommerce-error > li")
element_check = element.text
assert element_check == "Please enter a coupon code."

time.sleep(2)
driver.quit()

#Shop: покупка товара

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")

driver.find_element_by_css_selector("#menu-item-40 > a").click()

driver.execute_script("window.scrollBy(0, 500);")
driver.find_element_by_css_selector("[data-product_id='165']").click()
time.sleep(2)
driver.find_element_by_css_selector(".wpmenucart-contents > i").click()

driver.find_element_by_css_selector(".checkout-button.button.alt.wc-forward").click()

wait = WebDriverWait(driver,10)

login = wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
login.send_keys("Mind")
driver.find_element_by_id("billing_last_name").send_keys("M1nd")
driver.find_element_by_id("billing_email").send_keys("maks_ivanov_32@bk.ru")
driver.find_element_by_id("billing_phone").send_keys("+797365732431")

driver.find_element_by_id("select2-chosen-1").click()
driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
time.sleep(1)
driver.find_element_by_css_selector(".select2-results-dept-0.select2-result.select2-result-selectable").click()

driver.find_element_by_id("billing_address_1").send_keys("st 111, d-2")
driver.find_element_by_id("billing_city").send_keys("SPB")

driver.find_element_by_id("billing_state").send_keys("MSC")

driver.find_element_by_id("billing_postcode").send_keys("670000")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
driver.find_element_by_id("payment_method_cheque").click()

driver.find_element_by_id("place_order").click()

thsu = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
print(" напись Thank you. Your order has been received отображается")
pm  = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>tr:nth-child(3)>td"), "Check Payments"))
print("надпись Check Payments отображается")






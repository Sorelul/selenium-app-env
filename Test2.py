from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
driver.get("https://www.timeanddate.com/date/durationresult.html?d1=&m1=&y1=&d2=&m2=&y2=")
driver.implicitly_wait(30)

try:
    button_accept = driver.find_element("class name", "css-47sehv")
    button_accept.click()
except:
    print("No modal window found to close")


day1 = driver.find_element("id","d1")
month1 = driver.find_element("id","m1")
year1 = driver.find_element("id","y1")
day1.send_keys("01")
month1.send_keys("01")
year1.send_keys("2019")

day2 = driver.find_element("id","d2")
month2 = driver.find_element("id","m2")
year2 = driver.find_element("id","y2")
day2.send_keys("01")
month2.send_keys("01")
year2.send_keys("2021")

submit_button = driver.find_element("id","subbut2")
submit_button.click()

WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "bx-result"))
)

# get the first h2 inside the div with class bx-result
result = driver.find_element("css selector", "div.bx-result h2").text

print(result)

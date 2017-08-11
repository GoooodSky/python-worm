from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://pan.baidu.com/s/1c16S7z6")
driver.refresh()
elem = driver.find_element_by_id("accessCode")
elem.send_keys("vmld")
elem.send_keys(Keys.RETURN)

btn = driver.find_elements_by_xpath("//a[@class='g-buttons']")
btn.click()

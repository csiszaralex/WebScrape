from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login")
  return driver

def clean_text(text):
  """Extract only the temp from text"""
  out = float(text.split(": ")[1])
  return out

def main():
  driver = get_driver()
  driver.find_element("id","id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element("id", "id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  driver.find_element("xpath", "/html/body/nav/div/a").click()
  return 
  

print(main())
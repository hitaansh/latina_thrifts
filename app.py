import requests
import urllib
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(ChromeDriverManager().install())
url = ("https://www.depop.com/latinathrifts/")
driver.get(url)
wait = WebDriverWait(driver, 2000)

cookies = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/button[2]")
cookies.click()


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

load_more_path = "html/body/div/div/main/div[2]/div/div/button"

while check_exists_by_xpath(load_more_path):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    load_more = wait.until(EC.element_to_be_clickable((By.XPATH, "html/body/div/div/main/div[2]/div/div/button")))
    load_more.click()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)








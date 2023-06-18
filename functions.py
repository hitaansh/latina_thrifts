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


class Functions:
    def __init__(self):
        chrome_options.add_argument('--headless')                                       
        chrome_options.add_argument('--no-sandbox')                                     
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 2000) 

    def open_page(self, url):
        self.driver.get(url)
    
    def check_exists_by_xpath(self, xpath):                                               
        try:                                                                        
            self.driver.find_element_by_xpath(xpath)                                     
        except NoSuchElementException:                                              
            return False                                                            
        return True

    def click_button(self, path):
        button = self.driver.find_element(By.XPATH, path)
        button.click()

    def load_more(self, path):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        load_more = self.wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        load_more.click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)

    def press_product(self, path):
        product = self.wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        product.click()
        time.sleep(1)

        

    def back(self):
        self.driver.back()

    def quit_driver(self):
        self.driver.quit()


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
            driver.find_element_by_xpath(xpath)                                     
        except NoSuchElementException:                                              
            return False                                                            
        return True

    def load_more(self, path):
        return

    def quit_driver(self):
        self.driver.quit()


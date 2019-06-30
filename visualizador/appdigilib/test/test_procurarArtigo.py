# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestProcurarArtigo():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_procurarArtigo(self):
    # Test name: Procurar Artigo
    # Step # | name | target | value | comment
    # 1 | open | http://127.0.0.1:8000/ |  | 
    self.driver.get("http://127.0.0.1:8000/")
    # 2 | setWindowSize | 1299x608 |  | 
    self.driver.set_window_size(1299, 608)
    # 3 | click | name=search |  | 
    self.driver.find_element(By.NAME, "search").click()
    # 4 | type | name=search | RECVisu | 
    self.driver.find_element(By.NAME, "search").send_keys("RECVisu")
    # 5 | click | css=.btn-primary |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    if EC.text_to_be_present_in_element((By.ID, 'content1'), 'RECVisu'):
      print("Sucess")
    print("Error")


  

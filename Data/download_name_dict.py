from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import selenium
import time
import os

ENCODING = "utf-8"

path = "chromedriver_win32"
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
name_file_path = 'name dictionary/'
driver.get("http://hleventustun.com/isimlersozlugu.php?isim=erkek&sec=Se%C3%A7")

filename = os.path.join(name_file_path, "female.html")
if not os.path.exists(filename):
    driver.find_element(By.XPATH, "/html/body/div/div[6]/div[2]/div/form[2]/p[1]/input[1]").click() 
    
    sec_button = driver.find_element(By.XPATH, "/html/body/div/div[6]/div[2]/div/form[2]/p[2]/input")
    sec_button.click()
    filtre = Select(driver.find_element(By.XPATH, "/html/body/div/div[6]/div[2]/div/table/tbody/tr/td/form/table/tbody/tr/td[2]/select"))
    filtre.select_by_index(1) # selecting all the letters
    content = driver.page_source
    
    out_file = open("name dictionary/female.html", "w", encoding = ENCODING)
    out_file.write(content)

filename = os.path.join(name_file_path, "male.html")
# repeat all the steps with different values for males this time
if not os.path.exists(filename):
    driver.find_element(By.XPATH, "/html/body/div/div[6]/div[2]/div/form[2]/p[1]/input[2]").click() 
    
    sec_button = driver.find_element(By.XPATH, "/html/body/div/div[6]/div[2]/div/form[2]/p[2]/input")
    sec_button.click()
    filtre = Select(driver.find_element(By.XPATH, "/html/body/div/div[6]/div[2]/div/table/tbody/tr/td/form/table/tbody/tr/td[2]/select"))
    filtre.select_by_index(1) 
    content = driver.page_source
    out_file = open("name dictionary/male.html", "w", encoding = ENCODING)
    out_file.write(content)


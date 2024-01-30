from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import selenium
import time
import os


ENCODING = "utf-8"

# path = "C:/Users/aygun/OneDrive/Belgeler/CS210 Project/chromedriver_win32"
path = "chromedriver_win32"
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
assembly_file_path = 'assembly html files/'
driver.get("https://www.tbmm.gov.tr/Kutuphane/MazbataArama")
for i in range(1, 28):
    file_name = 'assembly_no{}.html'.format(i)
    try:
        file_path = os.path.join(assembly_file_path, file_name)
        if not os.path.exists(file_path):
            # if it is in the interval 1961 - 1977 it is saved
            # in a different format with a different naming
            if i in range(12,17): 
                select_value = "4-{}".format(i-11)
            else:
                select_value = "1-{}".format(i)

            se =  Select(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/form/div[4]/div/select"))
            time.sleep(2) # sleep to imitate human behavior
            se.select_by_value(select_value)
            sorgula_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/form/div[6]/div/button")
            time.sleep(0.5)
            sorgula_button.click()
            
            time.sleep(1)
            content = driver.page_source # get the content
            time.sleep(1)

            out_file = open("assembly html files/assembly_no{}.html".format(i), "w", encoding=ENCODING) # by using encoding parameter, we were able to deal with special characters
            out_file.write(content)
            time.sleep(1)
            # instead of creating a new driver object everytime
            # go to previous page with the existing one
            # for efficiency reasons
            driver.back() 
    except:
        print("A problem has occured in assembly no {}".format(i))


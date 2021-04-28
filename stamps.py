# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:29:27 2021

@author: Luke Samuel
"""

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

path = ("D:/SAMUEL/Softwares/chromedriver_win32/chromedriver.exe") #enter path to the chrome driver. (driver version should match your chrome version)
url = 'https://registration.telangana.gov.in/stampStockPosition.htm'

driver = Chrome(path) #, options = chrome_options)
driver.get(url)

xps = ['//*[@id="districtCode"]', '//*[@id="category"]', '//*[@id="denomination"]']
output = {}

for k in xps:
    x = driver.find_element_by_xpath(xps[k])
    options = [i for i in x.find_elements_by_tag_name("option")]
    var = [element.get_attribute("text")  for element in options if element.get_attribute("text") != "Select..."]
    output[k] = var
    
for a in output['district']:
    for b in output['category']:
        for c in output['denomination']:
            # print(a)
            # print(b)
            # print(c)  
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="districtCode"]'))).send_keys(a)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="category"]'))).send_keys(b)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="denomination"]'))).send_keys(c)  
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="stampStockRegister"]/div[3]/button[1]'))).click()
            driver.get(url)
    
    







# =============================================================================
# dump
# =============================================================================

# for a in output['district']:
#     print("\n")
#     for b in output['category']:
#         print("\n")
#         for c in output['denomination']:
#             print(a)
#             print(b)
#             print(c)  
            


































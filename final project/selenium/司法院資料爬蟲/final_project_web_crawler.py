# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
from bs4 import NavigableString
import pandas as pd



options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
#driver = webdriver.Firefox(options=options,executable_path=r'geckodriver.exe')
driver.get("https://law.judicial.gov.tw/FJUD/default.aspx")

driver.find_element(By.LINK_TEXT, "更多條件查詢").click()
driver.find_element(By.ID, "dy1").send_keys("109")
driver.find_element(By.ID, "dm1").send_keys("12")
driver.find_element(By.ID, "dd1").send_keys("1")
driver.find_element(By.ID, "dy2").send_keys("109")
driver.find_element(By.ID, "dm2").send_keys("12")
driver.find_element(By.ID, "dd2").send_keys("31")
# 109/1/1~109/1/15
driver.find_element(By.ID, "jud_jmain").send_keys("酒精")
driver.find_element(By.ID, "jud_kw").send_keys("公共危險")
driver.find_element(By.CSS_SELECTOR, ".main").click()
driver.find_element(By.ID, "btnQry").click()
driver.switch_to.frame(0)
driver.find_element(By.ID, "hlTitle").click()
'''
cnt=1
all_text=[]

soup=BeautifulSoup(driver.page_source,"html.parser")
tmp=soup.find("div",class_="row").contents
for t in tmp:
    s=''
    if isinstance(t, NavigableString):
        continue
    for i in t.contents:
        if isinstance(i, NavigableString):
            continue
        temp_str=i.text.replace('\n','')
        clean_str = ' '.join(temp_str.split())
        s+=clean_str
    all_text.append(s)
    break
print(str(cnt)+' done.')
cnt+=1


for i in range(500):
    try:   
        driver.find_element(By.ID, "hlNext").click()
        soup=BeautifulSoup(driver.page_source,"html.parser")
        tmp=soup.find("div",class_="row").contents
        for t in tmp:
            s=''
            if isinstance(t, NavigableString):
                continue
            for i in t.contents:
                if isinstance(i, NavigableString):
                    continue
                temp_str=i.text.replace('\n','')
                clean_str = ' '.join(temp_str.split())
                s+=clean_str
            all_text.append(s)
            break
        print(str(cnt)+' done.')
        cnt+=1
    except:
        pass

df = pd.DataFrame(all_text)
df.to_csv('Result_12.csv')

'''






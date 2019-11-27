import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_argument('headless')


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import time

driver  = webdriver.Chrome("E:\Tester\selenium\chromedriver.exe")
driver.maximize_window()
url = "https://chartink.com/dashboard/78"

driver.get(url)
time.sleep(4)

Details = driver.find_element_by_xpath("//div[contains(text(),'Daily volume')]")
query = driver.find_element_by_xpath("//div[@class='lg:flex flex-col flex-1']//div[3]//div[1]//div[1]//div[1]//div[2]//div[2]//span[1][contains(text(),'View Query')]")
Result=driver.find_element_by_xpath("//div[@class='flex items-center px-8 py-2 mr-2 border rounded-lg rounded-b-none cursor-pointer atlas-tabs-top-inactive'][contains(text(),'Result')]")
Table = driver.find_element_by_xpath("//span[contains(text(),'Table')]")
actions = ActionChains(driver)
actions.move_to_element(Details)
time.sleep(3)
actions.move_to_element(query).click().perform()
time.sleep(3)
'''actions.move_to_element(Result).click().perform()
time.sleep(2)
actions.move_to_element(Table).click().perform()'''
time.sleep(3)
content = driver.page_source
formatted = bs(content,features='lxml')
name = []
number_val=[]
table_details = formatted.find('table',attrs={'class':'vgt-table bordered'})
td = table_details.find_all('td',attrs={'class':'vgt-left-align'})
for i in td:
    name.append(i.text)
td_value = table_details.find_all('td',attrs={'class':'vgt-right-align'})
for n in td_value:
    number_val.append(n.text)



driver.close()
driver.quit()

df = pd.DataFrame({'Name':name,'value':number_val})
df['Name'] = df['Name'].str.replace("  ","")
df['Name'] = df['Name'].str.replace("\n","")
df['value'] = df['value'].str.replace("  ","")
df['value'] = df['value'].str.replace("\n","")

df.to_csv('chartindex.csv', index=False, encoding='utf-8') # writes data to csv file
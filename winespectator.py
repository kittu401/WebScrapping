
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_argument('headless')
data_score=[]
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import time
driver  = webdriver.Chrome("E:\Tester\selenium\chromedriver.exe")
driver.maximize_window()
url = "https://www.winespectator.com/vintagecharts/search/id/15"
driver.get(url)
time.sleep(6)
content = driver.page_source
data = bs(content, features='lxml')
table = data.find('table',attrs={'class':'table table-condensed'})
td = data.find_all('td')

for i in td:
    data_score.append(i.text)
df = pd.DataFrame(data_score,columns=['data'])
df_new = df[df['data'].str.contains("Score")]
df_new["data"] = df_new["data"].str.replace("Score", "")
df_new.to_csv('data_score.csv')
driver.quit()
driver.close()
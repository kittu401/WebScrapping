# Import required Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_argument('headless')
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
Addr = []
Number = []
Url = []
new =[]
driver  = webdriver.Chrome("E:\Tester\selenium\chromedriver.exe",chrome_options=options)
driver.maximize_window()
i = 1

while i <95:#--->  total page numbers
    url = "https://seguro.ifema.es/waCatalogoMovil/waCatalogoWeb/index.html?idioma=en&feria=FT19&fbclid=IwAR1JP6etj-MbCl1OOMPvkjaW7xLpDS9KrZz0MmjleEYpDLcjOcmcyBR-vE8#LSECTOR&p=1&i=en&t=TODO&e=100&b=&s=93"
    print("page number is "+str(i))
    driver.get(url)
    time.sleep(3)
    content = driver.page_source
    formatted = bs(content,features='lxml')

    Title = formatted.findAll('label',attrs={'class':'pull-left tituloEmrpesa'}) # gets Company names

    for x in Title:
        name = str(x.text)
        print(name)
        new.append(name)
        if content.find(name):
            if "'" in name:
                text = driver.find_element_by_xpath("//label[text()=\"" + name + "\"]")
                time.sleep(5)
                text.click()
                time.sleep(10)
                address1 = driver.find_element_by_id("lbDireccion").text # block for getting address details
                address2 = driver.find_element_by_id("lbCP").text
                address3 = driver.find_element_by_id("lbPoblacion").text
                address4 = driver.find_element_by_id("lbProvincia").text
                address5 = driver.find_element_by_id("lbPais").text
                line = address1 + address2 + address3 + " " + address4 + address5
                Addr.append(line)

                xpath = "//span[@id='lbTel']"
                #  Gets Phone Number
                try:
                    num = driver.find_element_by_xpath(xpath).text
                    Number.append(num)
                except:
                    Number.append("Not Available")

                # Gets  Web Address

                try:
                    link = driver.find_element_by_css_selector("#lbWeb").get_attribute("href")
                    Url.append(link)
                except:
                    Url.append("No Link Available")
                driver.back()
                time.sleep(5)
            else:
                text = driver.find_element_by_xpath("//label[contains(text(),'" + name + "')]")
                time.sleep(5)
                WebDriverWait(driver, 10)
                text.click()

                time.sleep(10)
                address1 = driver.find_element_by_id("lbDireccion").text
                address2 = driver.find_element_by_id("lbCP").text
                address3 = driver.find_element_by_id("lbPoblacion").text
                address4 = driver.find_element_by_id("lbProvincia").text
                address5 = driver.find_element_by_id("lbPais").text
                line = address1 + address2 + address3 + " " + address4 + address5 # comnbibes all address blocks to Single line
                Addr.append(line)

                xpath = "//span[@id='lbTel']"
                # Phone Number
                try:
                    num = driver.find_element_by_xpath(xpath).text
                    Number.append(num)
                except:
                    Number.append("Not Available")

                # Web Address

                try:
                    link = driver.find_element_by_css_selector("#lbWeb").get_attribute("href")
                    Url.append(link)
                except:
                    Url.append("No Link Available")
                driver.back()
                time.sleep(3)
    i=i+1
driver.close()
driver.quit()

df = pd.DataFrame({'Title':new,'Address':Addr,'Number':Number,'link':Url}) # writes data frame in to excel file

df.to_csv('facebook.csv', index=False, encoding='utf-8') # writes data to csv file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

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
print("driver launched")
url = "https://seguro.ifema.es/waCatalogoMovil/waCatalogoWeb/index.html?idioma=en&feria=FT19&fbclid=IwAR1JP6etj-MbCl1OOMPvkjaW7xLpDS9KrZz0MmjleEYpDLcjOcmcyBR-vE8#LSECTOR&p=1&i=en&t=TODO&e=100&b=&s=93"
driver.get(url)
print("url found")
time.sleep(3)
sector = driver.find_element_by_xpath("//button[@id='S']")
sector.click()
time.sleep(4)

# select xpath for required sector 

lable = driver.find_element_by_xpath("//label[@class='lblEmpresasBusquedaSimpleNegrita'][contains(text(),'Transport')]")
lable.click()
time.sleep(5)
i = 1
while i <4:
    print( "page number "+str(i))
    url2 ="https://seguro.ifema.es/waCatalogoMovil/waCatalogoWeb/index.html?idioma=en&feria=FT19&fbclid=IwAR1JP6etj-MbCl1OOMPvkjaW7xLpDS9KrZz0MmjleEYpDLcjOcmcyBR-vE8#LSECTOR&p="+str(i)+"&s=6&t=TODO&e=100&b=&s=6"
    driver.get(url2)
    time.sleep(15)
    content = driver.page_source
    formatted = bs(content, features='lxml')

    Title = formatted.findAll('label', attrs={'class': 'pull-left tituloEmrpesa'})

    # Company Title

    for x in Title:
        name = str(x.text)
        print(name)
        new.append(name)
        if content.find(name):
            if "'" in name:
                try:
                    text = driver.find_element_by_xpath("//label[text()=\"" + name + "\"]")
                    time.sleep(15)
                    text.click()
                except Exception as e:
                    print('exception raised : ' + name)

                    driver.get(url2)
                    print("url found")

                    time.sleep(6)
                    content = driver.page_source
                    formatted = bs(content, features='lxml')
                    text = driver.find_element_by_xpath("//label[text()=\"" + name + "\"]")
                    time.sleep(15)
                    text.click()

                time.sleep(10)
                address1 = driver.find_element_by_id("lbDireccion").text
                address2 = driver.find_element_by_id("lbCP").text
                address3 = driver.find_element_by_id("lbPoblacion").text
                address4 = driver.find_element_by_id("lbProvincia").text
                address5 = driver.find_element_by_id("lbPais").text
                line = address1 + address2 + address3 + " " + address4 + address5
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
                time.sleep(5)
            else:
                try:
                    text = driver.find_element_by_xpath("//label[contains(text(),'" + name + "')]")
                    text.click()
                except Exception as e:
                    print('excepion raised : ' + name)
                    driver.get(url2)
                    print("url found")

                    time.sleep(6)
                    content = driver.page_source
                    formatted = bs(content, features='lxml')
                    text = driver.find_element_by_xpath("//label[contains(text(),'" + name + "')]")
                    time.sleep(15)
                    text.click()

                time.sleep(10)
                address1 = driver.find_element_by_id("lbDireccion").text
                address2 = driver.find_element_by_id("lbCP").text
                address3 = driver.find_element_by_id("lbPoblacion").text
                address4 = driver.find_element_by_id("lbProvincia").text
                address5 = driver.find_element_by_id("lbPais").text
                line = address1 + address2 + address3 + " " + address4 + address5
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
    i = i+1
driver.close()
driver.quit()

df = pd.DataFrame({'Title':new,'Address':Addr,'Number':Number,'link':Url})

df.to_csv('transport.csv', index=False, encoding='utf-8')
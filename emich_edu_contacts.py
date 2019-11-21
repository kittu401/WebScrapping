import csv
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import time

url = "https://www.emich.edu/contacts/index.php"

r = requests.get(url)
contacts=[]
time.sleep(5)
data = bs(r.text, features='lxml')
div = data.find_all('div',attrs={'class':'large-4 small-12 column'})
for anchor_tag in div:
    anchor = anchor_tag.find_all('a')
    for contact in anchor:
        contacts.append(contact.text)

df = pd.DataFrame({'Contacts': contacts})
df.to_csv('contact_details.csv', encoding='utf-8',index=0)
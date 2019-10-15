import csv

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import time

data_count=[]
name =[]
final =[]
dataset_count = []
date_details = []
url = "https://www.data.gov/metrics"

r = requests.get(url)

time.sleep(5)
data = bs(r.text, features='lxml')
div = data.find('div',attrs={'class':'single'})
# title = div.find_all('div',attrs={'class':'row agencytitle'})
div2= div.find_all('div',attrs={'class':'view-content'})
for table in div2:
    td = table.find('table',attrs={'class':'views-table cols-4 datasets_published_per_month_table'})
    trow =td.find_all('tr',attrs={'class':'datasets_published_per_month_row_tr_odd odd parent-agency'})
    for table_body in trow:
        tbody = table_body.find_all('td', attrs={'class': 'datasets_published_per_month_table_row_fields'})
        for data in tbody:
            data_count.append(data.text)

num =0
for i in data_count:
    while num < len(data_count):
        name.append(data_count[num])
        num = num +1

for details in name:
    num =0
    while num < len(name):
        final.append(name[num])
        num = num + 3
for count in name:
    num = 1
    while num < len(name):
        dataset_count.append(name[num])
        num = num + 3
for date in name:
    num = 2
    while num < len(name):
        date_details.append(name[num])
        num = num + 3
df = pd.DataFrame({'DataSets': final,'Count':dataset_count,'Date':date_details})
df_new = df.drop_duplicates()
df_new.to_csv('datasets.csv', encoding='utf-8',index=0)





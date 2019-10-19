import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
links = []
src_links =[]
photo_id = []
url = "https://x.yupoo.com/photos/xiaoxiao0723/albums?tab=gallery"
url2 ="https://x.yupoo.com"
r= requests.get(url)
data = bs(r.text, 'html.parser')
a_tag = data.find_all('a',attrs={'class':'album__main'})
for i in a_tag:
    links.append(i.get('href'))# for getting Href links from the website

for img_detials in links:
    image_link =requests.get(url2+img_detials)
    images = bs(image_link.text, 'html.parser')
    img_link = images.find_all('div',attrs={'class':'image__imagewrap'})

    for x in img_link:
        src_links.append(x.find('img')['src'])
        photo_id.append(x.find('div')['data-photoid'])



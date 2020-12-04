import requests
from bs4 import BeautifulSoup
import os
import wget

url = 'https://vpnbook.com/'

r = requests.get(url)
soup = BeautifulSoup(r.content,'html5lib')
raw_link = soup.select('#pptpvpn > ul:nth-child(1) > li:nth-child(11) > strong:nth-child(1) > img:nth-child(1)')
link = url+raw_link[0].get('src').split(" ")[0]
wget.download(link,out='vpn_pass.png')
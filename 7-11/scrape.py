import requests
import sys
from bs4 import BeautifulSoup

# # print bitcoin, xrp, dogecoin prices in order
# urlList = ["https://www.coindesk.com/price/bitcoin/","https://www.coindesk.com/price/xrp/","https://www.coindesk.com/price/dogecoin/"]

def printPrices(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	prices = soup.find_all("span", class_="typography__StyledTypography-owin6q-0 jvRAOp")
	for price in prices:
	    print(price.text, end="\n")

urlList = []
prefix = "https://www.coindesk.com/price/"
for arg in sys.argv:
	if arg != "scrape.py":
		# print(arg,end="\n")
		urlList.append(prefix+arg)

# because argv[0] is the filename
for index,url in enumerate(urlList,start=1):
	print(sys.argv[index]+" :")
	printPrices(url)


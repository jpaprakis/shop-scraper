from bs4 import BeautifulSoup
import pdb


f = open('tempfile', 'r')
data = f.read()
#pdb.set_trace()
soup = BeautifulSoup(data, "html.parser")

tags = soup.findAll('li',  { "class" : "grid-tile" })
#pdb.set_trace()
for tag in tags:

	#print(tag)

	#IMAGE
	img_url = tag.find('a', { "class" : "thumb-link" } ).img['src']
	#print(img_url)
	#NAME AND URL
	name_and_url = tag.find('a', { "class" : "name-link" } )
		#NAME
	#print(name_and_url.string.strip())
		#URL
	#print(name_and_url['href'])
	#pdb.set_trace()
	prices = tag.find('div', { "class": "product-pricing" })
	#This only happens if there's sales/promos
	if prices.div != None:
		spans = prices.div.findAll('span')
		for span in spans:

			#REGULAR PRICE
			if span['class'][0] == 'product-standard-price':
				if span.string:
					print(span.string.strip())
			
			#SALE PRICE
			elif span['class'][0] == 'product-sales-price':
				if span.string:
					print(span.string.strip())

	#Otherwise no sale/promo just take the inner price
	else:
		if prices.string:
			print(prices.string.strip())
	#print(prices)
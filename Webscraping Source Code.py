import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.hp.com/my-en/shop/laptops-tablets/laptop-gaming.html'

# Opening up connection, grabbing the page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")
product_list = page_soup.findAll("li",{"class":"product-item"})

# Write into csv file
filename = "webscraping_products.csv"
f = open(filename, "w")

headers = "Model Name, Product Number, Retail Price, Sale Price, Instalment Fee (12 Months), Stock Availability\n"
f.write(headers)

for product in product_list:

	# 1st attribute: Product name
	title_container = product.findAll("a", {"class": "product-item-link"})
	product_name = title_container[0].text.strip()

	# 2nd attribute: Product number
	pronum_container = product.findAll("div", {"class":"product-sku"})
	product_num = pronum_container[0].text

	price_container = product.findAll("span",{"class":"price"})

	# 3rd attribute: Retail price
	retail_price = price_container[0].text

	# 4th attribute: Discount price
	discount_price = price_container[2].text

	# 5th attribute: Installment fee for 12 months
	instalment_fee = price_container[3].text

	# 6th attribute: Stock availability
	stock_container = product.findAll("span",{"class":"stellar-body__extra-small"})
	product_stock = stock_container[0].text.strip()
	if product_stock == "Same Day Delivery*":
	    stock = "Yes (Same Day Delivery)"
	elif product_stock == "Out of stock: Call - 1800 88 4889":
	    stock = "No (Out of Stock)"

	print("\nModel Name: " + product_name)
	print("Product Number: " + product_num)
	print("Retail Price: " + retail_price)
	print("Sale Price: " + discount_price)
	print("Instalment Fee (12 Months): " + instalment_fee)
	print("Stock Availability: " + stock + "\n")

	f.write(product_name + "," + product_num + "," + retail_price.replace(",", "") + "," + discount_price.replace(",", "") + "," + instalment_fee + "," + stock + "\n")

f.close()
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://anycallmobilemm.com/product-category/smartphone/"

# Set up the driver
options = webdriver.FirefoxOptions()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)

driver.get(url)


# get product names
product_name_elements_list = driver.find_elements(By.CLASS_NAME, "wd-entities-title")

product_price_elements_list = driver.find_elements(By.CLASS_NAME, "price")
print(product_price_elements_list)

product_names_list = []
product_prices_list = []

for product in product_name_elements_list:
    product_name = product.text
    product_names_list.append(product_name)
    
for price in product_price_elements_list:
    price_text = price.text
    prices_list = price_text.split(" ")
    if len(prices_list) == 3:
        extracted_price = prices_list[1]
        extracted_price = extracted_price.replace("Ks", "")
        extracted_price = extracted_price.replace(",", "")
        extracted_price = float(extracted_price)
        product_prices_list.append(extracted_price)
        print(extracted_price)
    else:
        extracted_price = prices_list[0]
        extracted_price = extracted_price.replace(",", "")
        extracted_price = float(extracted_price)
        product_prices_list.append(extracted_price)
        print(extracted_price)
        
# Export Dataset
df = pd.DataFrame({"Product Name":product_names_list,
                   "Price":product_prices_list})

print(df.head())

df.to_excel("AnyCall Data.xlsx", index=False)


page_number_elements_list = driver.find_elements(By.CLASS_NAME, "page-numbers")

page_num_list = []
for page_num in page_number_elements_list:
    page_num = page_num.text
    try:
        page_num = int(page_num)
        page_num_list.append(page_num)
    except:
        continue

max_page_num = max(page_num_list)

print(max_page_num)
driver.close()

#Install required libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm
import time

def extract_max_page_num():

    ###### Step 1. Send request to the website
    url = "https://anycallmobilemm.com/product-category/smartphone/"

    #Send request to website
    response = requests.get(url)

    if response.status_code == 200:
        print("Connection is successful!")
        
        #Extract web content
        web_content = response.text
        
        #Prettify the web content and create as beautiful soup object
        bsobj = BeautifulSoup(web_content, 'html.parser')
        
            
        page_count_tag = bsobj.find('ul', class_='page-numbers')
        page_num_list = []

        for page_num in page_count_tag:
            page_num = page_num.text
            try:
                page_num = int(page_num)
                page_num_list.append(page_num)
            except:
                continue

        max_page_num = max(page_num_list)
        

        return max_page_num
    
#print(max_page_num)
#print(page_count_tag.text)

def extract_data(max_page_num):

    page_url = 'https://anycallmobilemm.com/product-category/smartphone/page/'
    name_list = []
    price_list = []
    link_list =[]

    for i in tqdm(range(max_page_num)):
        base_url = page_url + str(i+1) + "/"
        # Send request to website
        response = requests.get(base_url)
        
        if response.status_code == 200:
            print("Connection is successful!")

            #Extract web content
            web_content = response.text

            #Prettify the web content and create as beautiful soup object
            bsobj = BeautifulSoup(web_content, 'html.parser')

            #Extract all product tags of web page
            product_name_list = bsobj.find_all('h3', class_= 'wd-entities-title')
            #print(len(product_name_list)) # check counts of phones
            #product_tag = product_name_list[0]
            #print(product_tag)
            #print("\n")

            product_price_list = bsobj.find_all('span', class_= 'price')
        
            for product in product_name_list:
                product_name = product.text
                name_list.append(product_name)

            for price in product_price_list:
                product_price = price.text
                product_price = product_price.split(" ")
                #print(product_price)
                
                
                if len(product_price) == 3:
                    extracted_price = product_price[0]
                    extracted_price = extracted_price.replace(",", "")
                    extracted_price = extracted_price.replace("\xa0Ks", "")
                    extracted_price = extracted_price.replace("\xa0Ks", "")
                    extracted_price = float(extracted_price)
                    price_list.append(extracted_price)
                    
                else:
                    extracted_price = product_price[-1]
                    extracted_price = extracted_price.replace(",", "")
                    extracted_price = extracted_price.replace("\xa0Ks.", "")
                    extracted_price = extracted_price.replace("\xa0Ks", "")
                    extracted_price = float(extracted_price)
                    price_list.append(extracted_price)
                    
                    
            #print(name_list)
            #print(price_list)

    ########### Export as excel ############

    data_dic ={"Product Name" : name_list,
        "Price" : price_list}
    #create dataframe
    df = pd.DataFrame(data_dic)

    print(df.head())

    df.to_excel(r"AnyCall Data.xlsx", index = False)
        

#test
if __name__ == '__main__':
    maximum_page_number = extract_max_page_num()
    extract_data(maximum_page_number)


#errors has to be cleared

from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.amazon.in/Sony-PS5%C2%AE-Console-Cricket-Bundle/dp/B0CJ9JM214/ref=sr_1_1_sspa?crid=2GAC2OE3EZIH1&keywords=ps5&qid=1697400706&sprefix=ps5%2Caps%2C228&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

contents = response.text

soup = BeautifulSoup(contents, "html.parser")

name = soup.find("span", {"id": "productTitle"})
if name :
    product_name = name.get_text().strip()
else:
    product_name = "Product Name Not Found"

price_element = soup.find("span", {"id": "priceblock_ourprice"})
if price_element is None:
    price_element = soup.find("span", {"id": "priceblock_dealprice"})

if price_element:
    price = price_element.get_text().strip()
    print(f"The Price of {product_name} is Rs{price}")
else:
    print("Price information not found on the page.")

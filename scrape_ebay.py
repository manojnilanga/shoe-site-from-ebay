import requests
from bs4 import BeautifulSoup #pip install beautifulsoup4

url ="https://www.ebay.com/sch/i.html?_nkw=nike+shoes"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

item_list = soup.find_all("li", {"class":"s-item s-item__pl-on-bottom"})

print(len(item_list))
print(item_list[0])


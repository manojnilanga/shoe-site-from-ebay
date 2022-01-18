import requests
from bs4 import BeautifulSoup #pip install beautifulsoup4


def middleof(text, left,right,multi=False):
    if(not multi):
        try:
            middle = text.split(left)[1].split(right)[0]
            return middle
        except:
            return ""
    else:
        right_text=text
        items=[]
        while(True):
            try:
                item = right_text.split(left)[1].split(right)[0]
                items.append(item)
                right_text = right_text.split(left,1)[1].split(right,1)[1]
            except:
                break
        return items

url ="https://www.ebay.com/sch/i.html?_nkw=nike+shoes"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
items = middleof(response.text, "class=s-item__link href=","?",multi=True)
print(items)

item_count = 0
shoes_data = []
for item in items:
    if(item_count>9):
        break

    try:
        shoe = {}
        print("---------")
        print(item)
        response = requests.get(item)
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find("h1", {"id": "itemTitle"}).text.replace('Details about','').strip()
        print(name)
        shoe["name"]= name
        img = soup.find("img", {"id": "icImg"})["src"]
        print(img)
        shoe["img"] = img
        price = soup.find("span", {"id": "prcIsum"}).text.strip()
        print(price)
        shoe["price"] = price
        shoes_data.append(shoe)
        item_count += 1
    except Exception as e:
        print("Error ---> "+str(e))


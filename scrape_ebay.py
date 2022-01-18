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

# url ="https://www.ebay.com/sch/i.html?_nkw=nike+shoes"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# items = middleof(response.text, "class=s-item__link href=","?",multi=True)
# print(items)


item = "https://www.ebay.com/itm/234342309373"

response = requests.get(item)
print(response.text)
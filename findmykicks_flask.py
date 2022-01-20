from flask import Flask, render_template,request
import requests
from bs4 import BeautifulSoup #pip install beautifulsoup4

app = Flask(__name__)

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

def scrape_items(url):
    print("search url: "+url)
    response = requests.get(url)
    items = middleof(response.text, "class=s-item__link href=", "?", multi=True)
    print(items)

    item_count = 0
    shoes_data = []
    for item in items:
        if (item_count > 26):
            break

        try:
            shoe = {}
            print("---------")
            print("item url -> "+item)
            shoe["url"] = item
            response = requests.get(item)
            soup = BeautifulSoup(response.text, 'html.parser')
            name = soup.find("h1", {"id": "itemTitle"}).text.replace('Details about', '').strip()
            print(name)
            shoe["name"] = name
            img = soup.find("img", {"id": "icImg"})["src"]
            print(img)
            shoe["img"] = img
            price = soup.find("span", {"id": "prcIsum"}).text.strip()
            print(price)
            shoe["price"] = price
            shoes_data.append(shoe)
            item_count += 1
        except Exception as e:
            print("Error ---> " + str(e))

    return shoes_data

@app.route("/", methods=['GET', 'POST'])
def hello_world():

    if request.method == 'GET':
        return render_template('FindMyKicks.html')
    if request.method == 'POST':
        try:
            search_text = request.form["search-text"]
            if(search_text.strip()==""):
                return render_template('FindMyKicks.html')
            search_url = "https://www.ebay.com/sch/i.html?_nkw="+search_text.replace(" ","+")
            shoe_data = scrape_items(search_url)

            return render_template('FindMyKicks.html',shoe_data=shoe_data)
        except Exception as e:
            print("Error in POST method---> " + str(e))
            return render_template('FindMyKicks.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
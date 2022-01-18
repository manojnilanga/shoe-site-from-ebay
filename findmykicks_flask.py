from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():

    if request.method == 'GET':
        return render_template('FindMyKicks.html')
    if request.method == 'POST':
        shoe_data = [
            {
                'name':'Nike Air Jordan 1 Mid Banned Black Red White 554724-074 Mens and GS New',
                'img': 'https://i.ebayimg.com/images/g/mw4AAOSw-2JhvrjU/s-l500.jpg',
                'price': 'US $129.99'
            },
            {
                'name': "Nike Air Force 1 07 Low Triple Men's White 7-13 Casual CW2288-111 Shoes Sneakers",
                'img': 'https://i.ebayimg.com/images/g/8wgAAOSwQy1hLFZo/s-l500.jpg',
                'price' : 'US $67'
            }
        ]
        return render_template('FindMyKicks.html',shoe_data=shoe_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
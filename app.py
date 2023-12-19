from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def submit_form():
    name = request.form['name']
    gift_ideas = request.form['gift-ideas']
    comments = request.form['comments']
    
    form_data = f"Name: {name}\nGift Ideas: {gift_ideas}\nComments: {comments}\n"
    
    with open('wishlist.txt', 'a') as file:
        file.write(form_data)
    
    return 'Form data saved to wishlist.txt!'

if __name__ == '__main__':
    app.run(debug=True)

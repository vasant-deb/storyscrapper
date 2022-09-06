from flask import Flask, render_template, request, redirect

from flask import jsonify

import requests
from bs4 import BeautifulSoup
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def respond():
    
    URL = "https://realpython.github.io/fake-jobs/"
  
    #print(soup)
    # Return the response in json format
    return(URL)
    
@app.route('/check', methods=['GET'])
def home():
    URL = "https://thedarkestblog.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    title = soup.find(['title']).get_text()


    return jsonify({
            "data": soup,
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    #soup = BeautifulSoup(page.content, "html.parser")
    # # #print(soup)
    # # # Return the response in json format
    # # print(page)
   


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome API!",
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "No name found. Please send a name."
        })


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
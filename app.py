from flask import Flask, render_template, request, redirect

from flask import jsonify

import requests
from bs4 import BeautifulSoup

import json
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def respond():
    
    URL = "https://realpython.github.io/fake-jobs/"
  
    #print(soup)
    # Return the response in json format
    return(URL)
 
@app.route('/rs')
def someName():
    cur = mysql.connection.cursor()
    sql = "SELECT * FROM users"
    cur.execute(sql)
    results = cursor.fetchall()
    return(results)
    
 
@app.route('/check', methods=['GET'])
def home():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    r = requests.get("https://thedarkestblog.com/page/4/", headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    datas=[]
    image=''
# images = soup.findAll('img',{'class':'wp-post-image'})
# for img in images:
    # if img.has_attr('src'):
       # image=img['src']

    for each_div in soup.findAll('article',{'class':'type-post'}):
        for title in each_div.findAll('h1',{'class':'entry-title'}): 
            titlex=title.text
            
            
            for link in title.findAll('a'): 
                slugs=link.get('href')        
                
        
        for image in each_div.findAll('img',{'class':'wp-post-image'}): 
            imagex=image['src']
            
        rnew = requests.get(slugs, headers=headers)
        soup1 = BeautifulSoup(rnew.content, "html.parser")
        gdp_table = soup1.find("div", attrs={"class": "entry-content"})
            
        datas.append([{"image":imagex,"name": titlex,"slug": slugs,'desc':gdp_table.get_text()}])
        
       
    urlx = 'https://beta.autoreport.space/storyapi/public/createapi'
    json_string = json.dumps(datas)


    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    response = requests.post(urlx, data=json_string, headers=headers) 
    r_json=response.json()  
    return(r_json)

   
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

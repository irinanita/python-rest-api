from flask import Flask
import platform
import json
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/ping')
def pong():
    return "Pong"

@app.route('/system')
def system():
    system_info_dict = {"OS": platform.system(),
                   "Processor": platform.processor(),
                   "Python Version": platform.python_version()}
    system_info_json = json.dumps(system_info_dict)

    return system_info_json

@app.route('/mediainfo/<string:id>')
def mediainfo(id):
    print(id)
    response = requests.get('https://www.pond5.com/photo/' + id + '/') #retrieve the web page with our data
    '''
    We create a new BeautifulSoup object by passing 
    the constructor our newly acquired HTML content 
    and the type of parser we want to use:
    '''
    soup = BeautifulSoup(response.content, 'html.parser')
    our_image = soup.select_one('div[item_id="' + id + '"]').text
    #print(response.status_code)
    #print(dir(response))
    print(our_image)

    return "JSON object with image filename, size, dimensions and image title"

app.run(port=5000, debug=True)
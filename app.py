from flask import Flask
from flask import jsonify
import requests
import platform
import json
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import sys


app = Flask(__name__)


@app.route('/')
def home():
    return "This is an API in Python"

@app.route('/ping')
def pong():
    return "pong"

@app.route('/system')
def system():
    system_info_dict = {"Python API": "v1",
                   "OS": platform.system(),
                   "Processor": platform.processor(),
                   "Python Version": platform.python_version()}
    return jsonify(system_info_dict)


@app.route('/mediainfo/<string:id>')
def mediainfo(id):
        try:
            '''
            Retrieve the web page of the image with the specified id
            '''

            response = requests.get('https://www.pond5.com/photo/' + id + '/')

            '''
            Create a new BeautifulSoup object by passing 
            the constructor our acquired HTML content 
            and the type of parser we want to use :
            '''

            soup = BeautifulSoup(response.content, 'html.parser')

            '''
            Retrieve image title from the div element
            with the specific item_id that matches the
            <id> in the request
            '''

            image_formats_data_attirbute = soup.select_one('div[item_id="' + id + '"]')['formats_data']

            '''
            Retrieve the value of the attribute
            parse it to json and
            get the value corresponding to the key "title"
            '''
            formats_data_attirbute_json = json.loads(image_formats_data_attirbute )

            image_title = formats_data_attirbute_json['title']

            '''
            Retrieve image url from the img tag source attribute
            Split the link and retrieve the last element that reffers 
            to the filename
            '''
            url = soup.select_one('div[item_id="' + id + '"] img')['src']
            image_filename = url.split('/')[-1]

            '''
            Load image from url retrieved above
            and get size  
            '''
            data = requests.get(url).content
            im = Image.open(BytesIO(data))
            width, height = im.size
            size_bytes = sys.getsizeof(im.tobytes())

            image_info = {"Title": image_title,
                          "Filename": image_filename,
                          "Width": width,
                          "Height": height,
                          "Size(B)": size_bytes}

            return jsonify(image_info)
        except:
            return "An error occurred, please check if the url is correct."


app.run(port=5000, debug=False)
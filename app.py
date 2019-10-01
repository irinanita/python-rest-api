from flask import Flask
import requests
import platform
from bs4 import BeautifulSoup
import json
from PIL import Image
from io import BytesIO
import sys



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
    try:
        response = requests.get('https://www.pond5.com/photo/' + id + '/') #retrieve the web page with our data
        '''
        We create a new BeautifulSoup object by passing 
        the constructor our newly acquired HTML content 
        and the type of parser we want to use:
        '''
        soup = BeautifulSoup(response.content, 'html.parser') # parse the retrieved response
        #Retrieve image title
        our_image = soup.select_one('div[item_id="' + id + '"]')['formats_data']
        image_data = json.loads(our_image)
        print(image_data)
        print(image_data['title'])

        #Retrieve image url
        url = soup.select_one('div[item_id="' + id + '"] img')['src']
        image_filename = url.split('/')[-1]
        print(url)
        print(image_filename)

        data = requests.get(url).content
        '''
        Load image  
        '''
        im = Image.open(BytesIO(data))

        width, height = im.size

        print("img size in memory in bytes: ", sys.getsizeof(im.tobytes()))
        print(width, height)


        # Retrieve image title option 2 from DOM
        #image_title = soup.select_one('#itemDetail-mediaTitle span').text
        #print(image_title)

        return "JSON object with image filename, size, dimensions and image title"
    except:
        return "Something went wrong. Please check if the the endpoint is correct"
app.run(port=5000, debug=True)
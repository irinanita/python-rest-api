# Python API for Pond5

This is a REST API, made with Python 3.7 and Flask, which purpose is to retrieve image related data by DOM scraping
of [Pond5.com Website]('www.pond5.com')

## Run Locally
### Before You Start - Requiremenets
In order to copy the source files:
CD to the directory of your choice on your local machine and clone the repository from the terminal:

```
git clone https://github.com/irinanita/python-rest-api.git
```

Or you can download the the directory directly from GitHub.

> Apart from the `app.py` there is a `.idea` directory. You can ignore that, it refers to the IDE
info 

This API has been developed with Python 3.7. It should run with other Python 3 versions as well
if all the packages and models used match the version that is used.

In order to run this API locally the following packages/modules should be installed:
1. Install Python:
    * You can download it from the official website [Python Website]( http://www.python.org)
    * Or use a package manager. In my case I used Brew and the following command:
    ```
    brew install python3
    ```
2. Install a Python package manager. I used Pip. If you are using Python 3 and higher
 and downloaded from [Python Website]( http://www.python.org) 
 or if you are working in a Virtual Environment created by `virtualenv` or `pyvenv`
 pip will be already installed. Make sure to upgrade it [Documentation here]('https://pip.pypa.io/en/stable/installing/')   

> Remember if you have more than one version of Python on your machine you have to specify
the exact version. In my case all the commands had `python3.7` or `pip3.7`

3. Install the [Requests Library](https://pypi.org/project/requests/). It is used for
for making HTTP requests with Python. In my case the command I run in the terminal was:
```
pip3.7 install requests
``` 
> Remember to replace "3.7" with the version you are using on your machine

4. Install [Flask](https://palletsprojects.com/p/flask/), a Python microframework:
```
pip3.7 install flask
``` 

5. Install [Pillow](https://pypi.org/project/Pillow/). It's an Imaging Library:
```
pip3.7 install pillow
``` 

### Running
In order to run the API open the terminal, `cd` into the directory
containg `app.py file` and run the following command:

```python
python3.7 app.py
```

> Note that the port used in the app is 5000 if this port is occupied in your
 case you can change it and try running the app again
 
You should get something similar to this in your console:
```
Running on http://127.0.0.1:5000/  

```
Click on the link or copy and paste it into your browser.

### Using the API:
Once in the browser, there are three requests you can make to retrieve data:
1. Test purposes `/ping`
2. Information about the system, Python version and current API version `/system`
3. Information about a certain image `/mediainfo/<id>`. Where you have to specify the 
`<id>` of the image you are interested in. In case there is no such <id> you will get
an `Error Message`


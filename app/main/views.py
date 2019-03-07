from flask import render_template,request,redirect,url_for
from . import main
# from ..requests import get_photos,process_results
import requests
import json

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    r = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1337&api_key=lhryAfcIDBcWy2tlslGe7EYppRa44WueiXGJ1q8U').json()
    t = r['photos']
        
    camera = r['photos'][0]['camera']['name']
    rover = r['photos'][0]['rover']
    d = rover.keys()
    print(d)
    # for k,v in rover.items():
    #     # print(k)
    # # for key, value in s.items():
    #     # name = data.get('name')

    #     return (k,v)


    
    return render_template('index.html' ,t = t)



'''
This folder will make the app load slow when used
Instead, what should be here is at the views function

'''


# from . import main
# import urllib.request,json
# from .models import Rover
# import requests
# import json


# api_key = None

# base_url = None

# photos_url = None


# def configure_request(app):
#     global api_key,base_url,photos_url
#     api_key = app.config['ROVER_API_KEY']
#     base_url = app.config['ROVER_API_SOURCES_URL']

# def get_photos():
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_photos_url = base_url.format(api_key)

#     with urllib.request.urlopen(get_photos_url) as url:
#         get_photos_data = url.read()
#         get_photos_response = json.loads(get_photos_data)

#         photos_results = None

#         if get_photos_response['photos']:
#             photos_results_list = get_photos_response['photos']
#             # print (photos_results_list)
#             photos_results = process_results(photos_results_list)


#     return photos_results



# def process_results(photos_list):
#     '''
#     Function  that processes the news result and transform them to a list of Objects

#     Args:
#         photos_list: A list of dictionaries that contain photos details

#     Returns :
#         photos_results: A list of photos objects
#     '''
#     # photos_results = []
#     # for photo_item in photos_list:
#     #     date = photo_item.get('earth_date')
#     #     img_src = photo_item.get('img_src')
      
        
#     #     # photos_object = Rover(date,img_src)
#     #     # photos_results.append(photos_object)
#     #     print (date)

#     r = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1337&api_key=lhryAfcIDBcWy2tlslGe7EYppRa44WueiXGJ1q8U').json()
#     s = r['photos'][0]['camera']


        
#     return s

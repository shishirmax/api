import urllib3
import json
 
address_api = 'AIzaSyAnkNz_LwkyLkH5eosMfJNMNn0CZCcSCyU'
 
def locu_search(query):
    api_key = address_api
    adds = query.replace(' ', '%20')
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+adds
    final_url = url + "&key=" + api_key
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
   
    for item in data['results']:
        print (item['formatted_address'], item['geometry.location.lat'],item['geometry.location.lng'])
        #print item['results']
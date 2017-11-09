import requests
add = "new delhi"
r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=
"+add+"&key=AIzaSyAnkNz_LwkyLkH5eosMfJNMNn0CZCcSCyU")
r.status_code
#200
r.headers['content-type']
#'application/json; charset=UTF-8'
r.encoding
#'UTF-8'
r.text
'''
'{\n   "results" : [\n      {\n         "address_components" : [\n            {\
n               "long_name" : "New Delhi",\n               "short_name" : "New D
elhi",\n               "types" : [ "locality", "political" ]\n            },\n
          {\n               "long_name" : "Delhi",\n               "short_name"
: "DL",\n               "types" : [ "administrative_area_level_1", "political" ]
\n            },\n            {\n               "long_name" : "India",\n
       "short_name" : "IN",\n               "types" : [ "country", "political" ]
\n            }\n         ],\n         "formatted_address" : "New Delhi, Delhi,
India",\n         "geometry" : {\n            "bounds" : {\n               "nort
heast" : {\n                  "lat" : 28.65048,\n                  "lng" : 77.34
496009999999\n               },\n               "southwest" : {\n
   "lat" : 28.4041,\n                  "lng" : 77.07301009999999\n
 }\n            },\n            "location" : {\n               "lat" : 28.613939
1,\n               "lng" : 77.2090212\n            },\n            "location_typ
e" : "APPROXIMATE",\n            "viewport" : {\n               "northeast" : {\
n                  "lat" : 28.65048,\n                  "lng" : 77.3449600999999
9\n               },\n               "southwest" : {\n                  "lat" :
28.4041,\n                  "lng" : 77.07301009999999\n               }\n
     }\n         },\n         "place_id" : "ChIJLbZ-NFv9DDkRzk0gTkm3wlI",\n
    "types" : [ "locality", "political" ]\n      }\n   ],\n   "status" : "OK"\n}
\n'
'''
r.json()
'''
{'results': [{'address_components': [{'long_name': 'New Delhi', 'short_name': 'N
ew Delhi', 'types': ['locality', 'political']}, {'long_name': 'Delhi', 'short_na
me': 'DL', 'types': ['administrative_area_level_1', 'political']}, {'long_name':
 'India', 'short_name': 'IN', 'types': ['country', 'political']}], 'formatted_ad
dress': 'New Delhi, Delhi, India', 'geometry': {'bounds': {'northeast': {'lat':
28.65048, 'lng': 77.3449601}, 'southwest': {'lat': 28.4041, 'lng': 77.0730100999
9999}}, 'location': {'lat': 28.6139391, 'lng': 77.2090212}, 'location_type': 'AP
PROXIMATE', 'viewport': {'northeast': {'lat': 28.65048, 'lng': 77.3449601}, 'sou
thwest': {'lat': 28.4041, 'lng': 77.07301009999999}}}, 'place_id': 'ChIJLbZ-NFv9
DDkRzk0gTkm3wlI', 'types': ['locality', 'political']}], 'status': 'OK'}
'''
import json
json_r = r.json()
json_str = json.dumps(json_r)
parsed_json = json.loads(json_str)

#this gives the formatted address
print(parsed_json['results'][0]['formatted_address'])
#this gives the latitude
print(parsed_json['results'][0]['geometry']['location']['lat'])
#this gives the longitude
print(parsed_json['results'][0]['geometry']['location']['lng'])

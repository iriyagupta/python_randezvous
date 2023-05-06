import time
import folium
import webbrowser
import argparse
import sys, re, os
import pandas as pd
import numpy as np
import requests
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

#import pandas as pd
#from geopy.geocoders import Nominatim

def maps(args):
	geolocator = Nominatim(user_agent="myGeocoder", timeout=10)
	data = [
		{'Address': "Shuka NYC", 'Latitude': None, 'Longitude' :None},
	      ]
	print(data[0])
	data[0]["Address"].append(args.add)
	df = pd.DataFrame(data, dtype=str)
	df['city_coord']  = df['Address'].apply(geolocator.geocode)
	df['Latitude'] = df['city_coord'].apply(lambda x: (x.latitude))
	df['Longitude'] = df['city_coord'].apply(lambda x: (x.longitude))
	print(df[['Address', 'Latitude','Longitude']])
	m = folium.Map(location=[df.Latitude.mean(), df.Longitude.mean()], tiles="cartodbdark_matter", zoom_start=10, control_scale=True)

	#df = df.astype({'Latitude':'float'})
	#df = df.astype({'Longitude':'float'})
	#print([df.iloc[:,2].values])
	for i in range(0,len(data)):
	   folium.Marker(
	      location=[df.iloc[:,1].values, df.iloc[:,2].values],
	      popup=df.iloc[:,0].values,
	      icon = folium.Icon(color='red'),
	   ).add_to(m)

	m.save("map.html")
	webbrowser.open("map.html")
	#time.sleep(30)


###add the argparse method to pass in the directory for the user input
parser = argparse.ArgumentParser(description="get the map values")
#parser.add_argument('--lat', help='latitude', required = True)
#parser.add_argument('--lon', help='longitude', required = True)
parser.add_argument('--add', help='address', required = True)
args = parser.parse_args()

maps(args)


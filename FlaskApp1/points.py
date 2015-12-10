import pandas as pd
from geopy.distance import vincenty
from geopy.geocoders import Nominatim

def latlon_to_address(lat, lng):
	geolocator = Nominatim()
	location = geolocator.reverse("%s, %s" % (lat, lng))
	return location.address

def map_to_latlon(address):
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	# print location.address
	return location.address, location.latitude, location.longitude

def distance_cal(origin, destination):
	distance = vincenty(origin, destination).miles
	return distance

def list_points(origin, dist_limit=5):
	dist_limit = float(dist_limit)
	df = pd.read_csv("DATA/babs_master/station_master.csv")
	# print df.columns
	points = []
	min_dist=distance_cal(origin,(df['lat'][0], df['long'][0]))
	cl_loc = (df['lat'][0], df['long'][0])
	for i in range(len(df)):
		destination = (df['lat'][i], df['long'][i])
		dist=distance_cal(origin, destination)
		# print dist
		if dist < dist_limit:
			# print i
			points.append((df['lat'][i], df['long'][i]))
		if dist< min_dist:
			min_dist = dist
			cl_loc = (df['lat'][i], df['long'][i])

	return points, cl_loc

def closest(origin):
	df = pd.read_csv("DATA/babs_master/station_master.csv")
	drop_off = (df['lat'][0], df['long'][0])
	min_dist=distance_cal(origin, drop_off)
	# print min_dist
	for i in range(len(df)):
		destination = (df['lat'][i], df['long'][i])
		dist=distance_cal(origin, destination)
		# print min_dist, dist
		if dist < min_dist:
			min_dist = dist
			print min_dist
			drop_off = (df['lat'][i], df['long'][i])

	return drop_off
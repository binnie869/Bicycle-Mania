import numpy as np
import pickle
from datetime import datetime
from datetime import timedelta
from geopy.distance import vincenty
from geopy.geocoders import Nominatim

#features = ['month', 'day_of_month', 'hour_of_day', 'day_of_week', 'weekend', 'distance']

def weather_features(datetime):
	pass

def make_features(origin, destination, datetime):
	distance = vincenty(origin, destination).miles
	date = datetime.strptime(datetime, "%Y-%m-%dT%H:%M")
	month = date.month
	day_of_month = date.day
	hour_of_day = date.hour
	day_of_week = date.isoweekday()
	if date.isoweekday() in range(1, 6):
		weekend = 0
	else:
		weekend = 1
		return([month, day_of_month, hour_of_day, day_of_week, weekend, distance])

def prediction(origin, destination, datetime):
	xtest = make_features(origin, destination, datetime)
	my_classifier = pickle.load(open('rf_regressor_duration.pickle.pickle'))
	predicted = my_classifier.predict(xtest)
	return predicted

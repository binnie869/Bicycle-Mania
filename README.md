Bike Share Data Set: 
https://drive.google.com/drive/u/0/folders/0B23oaw39yOhlS0hKS01LbGNhZW8

File Structure
 - Weather data
 - Status data(available bike lockers and bikes at a station)
 - Trips
 - station to lat/long map



NYC Taxi Data location : http://www.andresmh.com/nyctaxitrips/
The  data is structured as:
	trip data like distance, time, location etc for Jan 13 to Dec 13 in 12 .csv files
	fare data like fare, tip, tolls, etc for Jan13 to Dec 13 in 12 .csv files
 
 Main code files:
 	visualization.ipynb - merge trip/fare data on a common key value and perform different visualizations.
 	Merge.sh/Merge.py - Merge data across all months and shuffle and write it to 1 csv file
 	Features&Modelling.ipynb - models and trip prediction.





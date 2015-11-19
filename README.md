Bike Share Data Set: On slack

NYC Taxi Data location : http://www.andresmh.com/nyctaxitrips/
The  data is structured as:
	trip data like distance, time, location etc for Jan 13 to Dec 13 in 12 .csv files
	fare data like fare, tip, tolls, etc for Jan13 to Dec 13 in 12 .csv files
 
 Main code files:
 	visualization.ipynb - merge trip/fare data on a common key value and perform different visualizations.
 	Merge.sh/Merge.py - Merge data across all months and shuffle and write it to 1 csv file
 	Features&Modelling.ipynb - models and trip prediction.





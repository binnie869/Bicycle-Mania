from flask import Flask, render_template, request
import points
import duration
import random

app = Flask(__name__)

content = '''
	<h1>Some title</h1>
'''

@app.route('/')
def show_index_page():
	return render_template('index.html')

@app.route('/query', methods=["POST", "PUT"])
def show_map():
	close_points = []
	origin = request.form.get("origin")
	destination = request.form.get("destination")
	radius = request.form.get("radius")
	date_time=request.form.get("datetime")
	orig, y_orig, x_orig = points.map_to_latlon(origin)

	dest, y_dest, x_dest = points.map_to_latlon(destination)
	# print y_orig, x_orig, y_dest, x_dest
	close_points, closest_start = points.list_points((y_orig, x_orig), radius)
	print closest_start[2]
	closest_drop = points.closest((y_dest, x_dest))
	dest_address = points.latlon_to_address(closest_drop[0], closest_drop[1])
	start_address = points.latlon_to_address(closest_start[0], closest_start[1])
	# print closest_drop
	bike_cnt = []
	dock_cnt =[]
	for i in range(len(close_points)):
		bike_cnt.append(random.randint(0,25))
		dock_cnt.append(random.randint(0, 25))
	# predicted_duration = random.random()
	#predicted_duration = duration.prediction(closest_start, closest_drop, date_time)
	lat =[]
	lng =[]
	name = []
	for point in close_points:
		lat.append(point[0])
		lng.append(point[1])
		name.append(point[2])


	return render_template("map.html", latitude=lat, longitude=lng, name=name, dock_cnt = dock_cnt,bike_cnt=bike_cnt, \
		 dest_lat= closest_drop[0], dest_bike_cnt=random.randint(0,25), dest_dock_cnt=random.randint(0,25), dest_long=closest_drop[1], dest_name =closest_drop[2], \
		 origin=[str(start_address)], destination=[str(dest_address)], \
		 cl_start_lat=closest_start[0], cl_start_long=closest_start[1], cl_start_name=closest_start[2], cl_bike_cnt=random.randint(0,25), cl_dock_cnt = random.randint(0,25), \
		 input_lat=y_orig, input_long=x_orig, output_lat=y_dest, output_long=x_dest)#, duration = predicted_duration)

@app.route('/trip', methods=["POST", "PUT"])
def show_route():
	print "HEEEERE"
	start = request.form.get('start_name')
	start_lat = request.form.get('start_lat')
	start_lng = request.form.get('start_lng')
	print start_lng
	dest = request.form.get('dest_name')
	dest_lat = request.form.get('dest_lat')
	dest_lng = request.form.get('dest_lng')
	print dest_lng
	predicted_duration = random.uniform(1,60)
	print "HEEERE 1"
	# return predicted_duration
	return render_template("trip.html", start_name = start, start_lat=start_lat, start_long=start_lng, \
	prediction=predicted_duration, dest_name=dest, dest_lat=dest_lat, dest_long=dest_lng)


if __name__ == '__main__':
	app.run(debug=True)



from flask import Flask, render_template, request
import points
import duration
import random

app = Flask(__name__)

content = '''
	<h1>Some title</h1>
'''

@app.route('/projects/')
def projects():
	return 'The projects page'


@app.route('/')
def show_index_page():
	return render_template('index.html')

@app.route('/query', methods=["POST", "PUT", "GET"])
def show_map():
	close_points = []
	origin = request.form.get("origin")
	destination = request.form.get("destination")
	radius = request.form.get("radius")
	# print radius
	date_time=request.form.get("datetime")
	orig, y_orig, x_orig = points.map_to_latlon(origin)

	dest, y_dest, x_dest = points.map_to_latlon(destination)
	print y_orig, x_orig, y_dest, x_dest
	close_points, closest_start = points.list_points((y_orig, x_orig), radius)
	closest_drop = points.closest((y_dest, x_dest))
	dest_address = points.latlon_to_address(closest_drop[0], closest_drop[1])
	start_address = points.latlon_to_address(closest_start[0], closest_start[1])
	# print closest_drop
	predicted_duration = random.random()
	#predicted_duration = duration.prediction(closest_start, closest_drop, date_time)
	lat =[]
	lng =[]
	for point in close_points:
		lat.append(point[0])
		lng.append(point[1])
	return render_template("map.html", latitude=lat, longitude=lng, dest_lat= closest_drop[0], \
		 dest_long=closest_drop[1], duration=predicted_duration, origin=start_address, destination=dest_address, \
		 cl_start_lat=closest_start[0], cl_start_long=closest_start[1], input_lat=y_orig, input_long=x_orig, \
		 output_lat=y_dest, output_long=x_dest)#, duration = predicted_duration)

if __name__ == '__main__':
	app.run(debug=True)



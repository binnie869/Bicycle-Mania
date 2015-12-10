from flask import Flask, render_template, request
#from nltk.corpus import words

app = Flask(__name__)
app.debug = True

content = '''
	<h1>Some title</h1>
'''

def some_function(word):
	return word

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return content + 'User %s' % username

@app.route('/projects/')
def projects():
	return 'The projects page'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/template/', methods=['GET', 'POST'])
def show_template(start=None, end=None, date=None):
	if request.method == 'POST':
	 	return render_template('hello.html', start=some_function(request.form['startAddress']), end=some_function(request.form['endAddress']), date=some_function(request.form['dateTime'])) 
	# else:
	# 	return render_template('hello.html')
	return render_template('hello.html', start=None, end=None, date=None)
	 

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
	app.run()



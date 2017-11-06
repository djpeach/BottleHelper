"""
This is just some example code for copy/pasteing.  For more detailed explainations, see the 
app_explained.py.
"""
# Imports
from bottle import route, run, template, request, post, get, error

# Basic Route
@route('/')
def index():
	return "<h1>Hello, world</h1><br><p>This is my home page!</p>"

# Route with Wildcard
@route('/hello/<name>')
def index(name):
	return template('index', name=name)

# Mulitple Binding to the same function
@route('/login')
@route('/signup')
def hello():
    return """<h1> This is the login/signup page.</h1>"""

# Using multiple binding to change function results
@route('/article/')
@route('/article/<id>')
def show_article(id=None):
	if not id:
		return ("This is the article homepage.")
	else:
		return ("You are viewing article number {}. Lets learn all the specifics of article {}...".format(id, id))

# Special 'static' routing for css, img, etc. files (internal use)
@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root="./static")

# Querying..idk much about this
@route('/querytest')
def querytest():
	p1 = request.query.p1 # hello
	p2 = request.query.p2 # world
	return "{}, {}".format(p1.capitalize(), p2)

# Speical '@get' route 
@get('/testform')
def form():
	return '''<form method="POST" action="/test">
				<input type="text" name="name1">
				<input type="submit" value="submit">
			  </form>'''
# Special '@post' route
@post('/test')
def submit():
	username = request.forms.get('name1')
	return "<h4>Hi there, {}</h4>".format(username)

# Basic error pages
@error(404)
def error404(error):
	return "You have exerienced a 404 error"

# Using json data...idk much about this
@route('/jsondata')
def jsondata():
	return {"name": "Jason", "List": [1,2,3,4,5]}

# Run the server
run(host='localhost', port=8080, debug=True, reloader=True)


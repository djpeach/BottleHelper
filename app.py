"""
This is just some example code for copy/pasting.  For more detailed explanations, see the
app_explained.py.
"""
# Imports
from bottle import route, run, template, request, post, get, error, static_file


# Basic Route
@route('/')
def index():
    return "<h1>Hello, world</h1><br><p>This is my home page!</p>"


# Route with URL Parameter
@route('/hello/<name>')
def index(name):
    return template('index', name=name)


# Multiple routes binding to the same function
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


# Querying (example url: `/search?firstName=Daniel&lastName=Peach` )
@route('/search')
def querytest():
    first_name = request.query.firstName
    last_name = request.query.lastName
    return "{}, {}".format(first_name, last_name)


# GET only route
@get('/form')
def form():
    return """"
    <form method="POST" action="/test">
        <input type="text" name="userName">
        <input type="submit" value="submit">
    </form>
"""


# POST only route
@post('/form')
def submit():
    username = request.forms.get('userName')
    return "<h4>Hi there, {}</h4>".format(username)


# Basic error pages
@error(404)
def error404(error):
    return "You have exerienced a 404 error"


# Using json data (useful for RESTful API's)
@route('/api')
def api():
    return {
        "name": "Jason",
        "List": [1, 2, 3, 4, 5]
    }


# Run the server (serve on your local host, on port 8080, set debug to true during development, and reloader to True to
# update as you make changes)
run(host='localhost', port=8080, debug=True, reloader=True)

"""
This is a file I put together of example Bottle.py Code to refer to during the project.
I could not find any great resources online, so I am going to make one that helps me,
and hopefully it helps anyone else too.  I have uploaded this to github at https://github.com/djpeach/BottleHelper/edit/master/app_explained.py , 
feel free to help update this and make it as helpful as possible.
"""
"""
>>> The first step is to download the Bottle file.
	You can either download this to your computer using pip, or download an actual file 
	to keep in your working directory. This allows you to import it into your project as you need to.
	To keep it super simple, go to this link: [bottle.py](https://raw.githubusercontent.com/bottlepy/bottle/master/bottle.py),
	select all the code, copy it, and paste it in a file. Save that file as `bottle.py`, and put it 
	in the same folder as your app.py
>>> The second step is to create two folders in the same directory as the Bottle file
	NAMES ARE IMPORTANT. Name one `views`, and the other `static`. The views folder is where you will
	store your web pages (your html files). The static folder is where you will store static files 
	(css, js, images, etc)
>>> The third step is to make your app.  Create your file, app.py, and code the app.
	Hopefully this document can help with that.
>>> The last step is to pull up your terminal and navigate to your directory with the app.py and bottle.py.
	run `python app.py` or `python3 app.py`, whichever you have set up.  Then open a browser and go to 
	localhost:8080/, or what ever host and port you set up up in the run command at the bottom. If you have IDLE, you can
	also open and run it there.
"""

# This imports all the necessary methods from the bottle.py file
from bottle import route, run, template, request, post, get, error

"""
Routes:
---------------
A route is how you read a request from your browser. When the user uses the browser url bar to go to www.mysite.com/form,
their browser sends a request to your server (app.py). That will be a GET request on the '/form' route. A GET request is 
just a semantic type of request that typically means the user wants to GET some content. (hence the name). On the other hand,
when a user submits a form that has a method="POST" and action="/form", you would get a POST request on the '/form' route.
This typically means the user wants to POST (aka create) data on your server.
"""

# '@route' lets your program read and make decisions based on the url bar in the browser.
@route('/')
# Here we define a function that gets run when the url bar is nothing but the default website.
# eg, www.website.com/
def index():
	# The function will return some sort of html to display to the user.
	# This is where the html comes in.
	return "<h1>Hello, world</h1><br><p>This is my home page!</p>"

# 'Wildcards' are how we start using the url to do things depending on what it says.
# The wildcard is what is in the <> brackets
@route('/hello/<name>')
# We take that wildcard, here it is 'name', and pass it into our function
# For www.website.com/daniel, name == daniel, and for www.website.com/jacob, name == jacob, and so on
def index(name):
	# Now we return some html in response, but instead of typing it here, we have a seperate file
	# containing our html code, its cleaner and easier this way.
	# We will also pass that html code the variable name as name, to use later in the page.
	# refer to 'example.html' to see this in use.
	return template('index.html', name=name) # Bottle looks in the folder 'views' when we use the keyword 'template'

# You can also route two different urls to the same function, therefor returning the same webpage.
@route('/login')
@route('/signup')
def hello():
    return """<h1> This is the login/signup page.</h1>"""


# This multible binding/routing can be useful for making decisions based on the wildcard
@route('/article/')
@route('/article/<id>')
# This function just determines if there is an id specified, and returns generic text if there is not,
# and more specific text if there is. 
def show_article(id=None):
	if not id:
		return ("This is the article homepage.")
	else:
		return ("You are viewing article number {}. Lets learn all the specifics of article {}...".format(id, id))

# Static Routes are a special route that are only used internally.
# They take in a filename as a wildcard, and pass it as a paramete to the function.
# To see this in use, check out the css links in the head of the example.html file.
@route('/static/<filename>')
# This function then uses the special keyword 'static_file' to get and return a static page(img, css, etc)
# to the appropriate place.
def server_static(filename):
	return static_file(filename, root="./static")


# Querying...honestly I am not to sure how this works, just watched a short video on it.
# I know that it allows us to get things from the browser's url and use them in some way.
# If you know more about this, please let me know what to put, or update it yourself.
@route('/querytest')
def querytest():
	p1 = request.query.p1 # hello
	p2 = request.query.p2 # world
	return "{}, {}".format(p1.capitalize(), p2)


# Notice this is not a typical @route. It is a @get route, which uses the GET method to get data and display it.
# I used this for my form to get data from the user and then I used the POST method when sending it to the 
# /testresult page on submit. See the next route to see how this works
@get('/testform')
def form():
	return '''<form method="POST" action="/test">
				<input type="text" name="name1">
				<input type="submit" value="submit">
			  </form>'''

# Notice this is not a typical @route. It is a @post route, which uses the POST method to send data to the server.
# I then use this page to get that data back from the form and use it in my html page.
@post('/test')
def submit():
	# the 'name1' lines up with the 'name' attribute of that input element from the html form on the /testform page.
	username = request.forms.get('name1')
	# then I use that to print out a greeting to that user.
	return "<h4>Hi there, {}</h4>".format(username)

# Notice this is not a typical @route. This is a special @error route.  This controls the pages the user sees for 
# various errors.  You pass in the specific error you want to make a page for and then define a function, passing
# in 'error'
@error(404)
def error404(error):
	# Normally this would be much prettier, probably using a template.
	return "You have exerienced a 404 error"

# Using json data
@route('/jsondata')
def jsondata():
	return {"name": "Jason", "List": [1,2,3,4,5]}

# This runs the actual server, always put it at the bottom.
# Some parameters it takes are used here below. host and port just specify the host and port to use, duh.
# debug just gives us some more info when we hit an error, so we can be lazy and not check our command line.
# reloader means that when you save the code, Bottle will automatically re-run your server without you having to
# quit it and start it up again manually (we can be lazy again, yay!)
run(host='localhost', port=8080, debug=True, reloader=True)

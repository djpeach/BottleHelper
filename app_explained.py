# This imports all the necessary methods from the bottle.py file
from bottle import route, run, template, request, post, get, error, static_file

"""
Routes:
---------------
A route is how your app receives a request from the user. For example, when the user enters a url into the browser bar 
and hits enter, that url gets sent to your app as a route. You define functions to handle these routes. 
"""

"""
Here we define a function that gets run when the url bar is nothing but the default website. (eg, www.website.com/)
"""


@route('/')
def index():
    """
    The most basic response from a function is a string, which may or may not contain html tags for markup
    """
    return "<h1>Hello, world</h1><br><p>This is my home page!</p>"


"""
A route can also contain variables which you can call 'wildcards' or route parameters. You catch this parameter by 
naming it in <>, and receiving it as an argument in your function. For example in the route defined as /<param>, if the 
user sends a request as /car, then in your function, param = car, but if the user sends a request to /home, then 
param = home. 
"""


@route('/hello/<name>')
def index(name):
    """
    Most times, you will want to return more than just a string. In order to return more complex html, bottle provides
    you with the ability to define html 'templates', which can accept arguments and interpret python code through
    special syntax. Remeber that only the simplest loops and logic should be used in the template, and most python logic
    should be performed in the function in your app.
    """
    return template('index.html', name=name)  # Bottle looks in the folder 'views' when we use the keyword 'template'


"""
You can also route two different urls to the same function, therefor returning the same webpage.
"""


@route('/login')
@route('/signup')
def hello():
    return """<h1> This is the login/signup page.</h1>"""


"""
This multible binding/routing can be useful for making decisions based on the route parameter
"""


@route('/article/')
@route('/article/<id>')
def show_article(id=None):
    """
    This function just determines if there is an id specified, and returns generic text if there is not,
    and more specific text if there is.
    """
    if not id:
        return "This is the article homepage."
    else:
        return "You are viewing article number {}. Lets learn all the specifics of article {}...".format(id, id)


"""
Static routes are a route that is used when you need to link to some static files. For example your css files or images.
To see this in use, check out the <link> tags in the html file used to link to our css. 

It makes use of route parameters to dynamically work for all static files.
"""


@route('/static/<filename>')
# This function then uses the special keyword 'static_file' to get and return a static page(img, css, etc)
# to the appropriate place.
def server_static(filename):
    """
    This function uses a special bottle function to tell the app where to find static files. We tell the function the
    name of the filename and where to look for our static files.
    """
    return static_file(filename, root="./static")


# Querying...honestly I am not to sure how this works, just watched a short video on it.
# I know that it allows us to get things from the browser's url and use them in some way.
# If you know more about this, please let me know what to put, or update it yourself.
@route('/querytest')
def querytest():
    p1 = request.query.p1  # hello
    p2 = request.query.p2  # world
    return "{}, {}".format(p1.capitalize(), p2)


"""
This is an example of using route query parameters. Whereas previous parameters were part of the url, these are appended
to the end of a regular url using the syntax of /route/?query1=something&query2=something+else

This sends a GET request to the server (our app), where we can receive them. This is often used for searches, since url
queries are publicly visible. You would never use url queries for any private information. For that you would use a POST
request. (more on this later)

This route would work for www.mysite.com/search/?firstName=Daniel&lastName=Peach
"""


@route('/search')
def querytest():
    first_name = request.query.firstName
    last_name = request.query.lastName
    return "{}, {}".format(first_name, last_name)


"""
For these next two functions, notice we define them with the same route of `/form`, however they take completely
different actions, depending on whether they are sent as a GET or POST request. If it is send as a GET request, then we 
know the user is requesting information, and we serve them up a form. Check out the next route to see what we do if we 
get a POST request.
"""


@get('/form')
def form():
    return """"
    <form method="POST" action="/test">
        <input type="text" name="userName">
        <input type="submit" value="submit">
    </form>
"""


"""
If we get a POST request on this route, we know the user has submitted a form using a method=POST, and they are sending 
us information. In that case, instead of sending them back a form, we grab that information via the request.forms.get()
function. Pass into this this function the name you gave your input. in our case, that name is userName (from the 
previous function's returned form)
"""


@post('/form')
def submit():
    username = request.forms.get('userName')
    return "<h4>Hi there, {}</h4>".format(username)


"""
Notice this is not a typical @route. This is a special @error route.  This controls the pages the user sees for
various errors.  You pass in the specific error you want to make a page for and then define a function, passing
in error as an argument
"""


@error(404)
def error404(error):
    # Normally this would be much prettier, probably using a template.
    return "You have exerienced a 404 error:\n {}".format(error)


"""
Turning your bottle app into a RESTful API instead of just a web server is as easy as returning json data instead of 
string or templates. A common practice here is to define a series of /api routes that return data to the client side. 
Once the client side receives this data, it can parse and do whatever it needs to with it. 
"""


@route('/api')
def api():
    return {"name": "Jason", "List": [1, 2, 3, 4, 5]}


"""
Run the server (serve on your local host, on port 8080, set debug to true during development, and reloader to True to 
update as you make changes)
"""
run(host='localhost', port=8080, debug=True, reloader=True)

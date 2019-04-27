# BottleHelper
Helping template for bottle.py for CS 230.

This is a file I put together of example Bottle.py Code to refer to during my school project. I could not find any great resources online, so I am going to make one that helps me, and hopefully it helps anyone else too.  I have uploaded this to github at https://github.com/djpeach/BottleHelper , feel free to help update this and make it as helpful as possible.

For additional information on Bottle, you can also check out the Bottle Docs themselves. 

[Official Bottle Documentation](https://bottlepy.org/docs/0.12/)

## Creating a Bottle App:

* The first step is to download the bottle.py file. You can either download this to your computer using pip, or download an actual file to keep in your working directory. This allows you to import it into your project as you need to.

	> To keep it super simple, you can go to this link: [bottle.py](https://raw.githubusercontent.com/bottlepy/bottle/master/bottle.py), select all the code, copy it, and paste it in a file. Save that file as `bottle.py`, and put it in the same folder as your app.py
	
* The second step is to create two folders in the same directory as the Bottle file *NAMES ARE IMPORTANT*. Name one folder `views`, and the other `static`. The views folder is where you will store your web pages (your html files). The static folder is where you will store static files  (css, js, images, etc)
* The third step is to make your app.  Create your file, app.py, and code the app.
	Hopefully this document can help with that.
* The last step is to pull up your terminal and navigate to your directory with the app.py and bottle.py. Run `python app.py` or `python3 app.py`, whichever you have set up.  Then open a browser and go to  localhost:8080/, or what ever host and port you set up up in the run command at the bottom.

    > If you have IDLE, you can also open and run it there.

from flask import Flask, render_template


#create a flask instance
app = Flask(__name__)

#FILTERS
#safe: This removes html tags from the screen display and prevents it from being displayed on the screen

#capitalize
#upper
#lower
#title: This will capitalize every letter in every word

#trim: this will remove spaces at the end

#striptags: This removes the html tags ad text totally


#create a route decorator
@app.route("/")

#def index():
	#return "<h1>Hello World!</h1>"

def index():
	first_name = "John"
	stuff = "This is <strong>Bold</strong> Text"

	favourite_pizza = ["Pepperoni", "Cheese", "Mushroom", 41]
	return render_template("index.html", 
		first_name=first_name,
		stuff=stuff,
		favourite_pizza=favourite_pizza)


#localhost:5000/user/john
@app.route("/user/<name>")

def user(name):
	return render_template("user.html", user_name=name)

#create custom error page

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500



#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/index")

#‘/’ URL is bound with first_flask function.
def first_webpage():
    name='Flask'

    return  render_template('index.html')

#run the application on local server
app.run()

#define a function with a different endpoint
@app.route("/Flask_2")
def second_flask():
    return "python is fun"

    #run using debug argument
app.run(debug=True)
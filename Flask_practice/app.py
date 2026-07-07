from flask import Flask

app=Flask(__name__)
#initialise the app wsgi

#create routes

#homepage route
@app.route("/") #this is a decorator which tell flask what url should trigger our function
def welcome():
    return "Welcome to my flask app!"

@app.route("/index")
def index():
    return "this is the index page"
    

if __name__=="__main__":
    app.run(debug=True) #the parameter debug=True will allow us to see the errors in the browser and also it will automatically restart the server when we make changes to the code similar to nodemon in nodejs, as soon as you save the file, the server will restart automatically
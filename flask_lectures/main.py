from flask import Flask,render_template

#render_template is a function that allows to render html templates and help in redirecting to html pages in website , used in route
'''
--> when this redirects to pages we need to create a floder named templates in same directory and with help of jinja2 template engine we can create html pages and redirect to them using render_template function
'''

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')
#if the file is not present in folder it will give template not found error and if the file is present it will redirect to that page

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)
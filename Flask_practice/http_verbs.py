'''
HTTP VERBS - get , post, put , delete
get-whenever we hit the url and we get the response and information
post-when we send the data to server and server will process it to give the reponse back to us
put-when we want to update the data in server
delete-when we want to delete the data from server

example-google browser default screen and when you serach and it returns
'''




from flask import Flask, render_template,request

#request--> helps in capturing the http requests

# WSGI Application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"


@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')
# if the file is not present in folder it will give template not found error and if the file is present it will redirect to that page


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form["name"]
        return f"Hello, {name}!"
    return render_template('form.html') #if not filling data just get the form page


if __name__ == "__main__":
    app.run(debug=True)

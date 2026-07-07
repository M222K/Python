from flask import Flask, render_template,request,redirect,url_for

# request--> helps in capturing the http requests

# WSGI Application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"


@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')
# if the file is not present in folder it will give template not found error and if the file is present it will redirect to that page


@app.route('/about')
def about():
    return render_template('about.html')

# #Variable rule example
# @app.route('/submit/<int:score>') #we can also assign variable rule such as only pass int value but then we have to typecast it in the function to as we can not concatenate int with string
# def submit(score):
#     return "The marks you got is "+str(score)

@app.route('/success/<int:score>')
def success(score):
    # res=""
    # if score>=50:
    #     res="PASS"
    # else:
    #     res="FAIL"
    return render_template('result.html',scores=score)#pass the result to the html page and we will use this dynamically paseed dat in the html page using jinja template engine by extracting using format {{results}} in the html page

# @app.route("/successif/<int:score>")
# def successif(score):
#     return render_template('result.html',scores=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', scores=score)

#example whether to redirect to pass or fail route as per the marks scored by the student
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        
        total_score=(science+maths+c+datascience)/4
    else:
        return render_template('getresults.html')
        
        #redirect the user to the success url using redirect and for the url
    return redirect(url_for('success',score=total_score))
        
    
if __name__ == "__main__":
    app.run(debug=True)

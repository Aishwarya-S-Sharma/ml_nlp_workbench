from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course.This should be an amazing course to learn Flask"

@app.route("/index",methods=['GET'])
def index():
    return "Welcome to the index page"

@app.route('/about')
def about():
    return "This is the about page of this Flask course"

if __name__=="__main__":
    app.run(debug=True)
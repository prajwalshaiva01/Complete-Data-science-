from flask import Flask


## WSGI application

app=Flask(__name__)


@app.route("/")
def welcome():
    return "welcome to Best Flask cource.This should be an amazing cource"

@app.route("/index")
def index():
    return "welcome to index page"

if __name__=="__main__":
    app.run(debug=True)


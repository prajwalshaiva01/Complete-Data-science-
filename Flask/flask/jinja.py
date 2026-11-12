 

from flask import Flask,render_template,request,redirect,url_for


## WSGI application

app=Flask(__name__)


@app.route("/")
def welcome():
    return "<html><H1>Welcome to the Flask cource</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')



@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

## variable rule
@app.route('/success/<int:score>')
def succes(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res="fail"

    return render_template('result.html',result=res)


@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res="fail"

    exp={'score':score,"res":res}

    return render_template('result1.html',result=exp)


## if condication
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result.html',result=score)

@app.route('/fail/<int:score>')
def fail(score):

    return render_template('result1.html',result=score)


@app.route('/form', methods=['POST', 'GET'])
def form():
  if request.method == 'POST':
    science = float(request.form['science'])
    math = float(request.form['math'])
    c = float(request.form['c'])
    data_science = float(request.form['datascience'])

    total_score = (science + math + c + data_science) / 4
    return redirect(url_for('successres', score=total_score))

  return render_template('getresult.html')




if __name__=="__main__":
    app.run(debug=True)



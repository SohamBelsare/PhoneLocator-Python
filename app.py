from flask import Flask,render_template, request, redirect
from logic import location
app=Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        pno = request.form['pno']
        print(pno)
        location(pno)
    return render_template('home.html')

@app.route('/loc',methods=['GET', 'POST'])
def locat():
    return render_template('myloc.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
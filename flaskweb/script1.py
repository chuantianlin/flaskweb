from flask import Flask
from flask import render_template
app=Flask(__name__)#name is the special python varible  it will assign __name__="__main__"
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/about/')
def about():
    return render_template("about.html")
if __name__=='__main__':
    app.run(debug=True) # if you assin the script to another script __name__="script1"

from flask import Flask, render_template, request
from multiprocessing import Pool
import webbrowser
import time

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def render():    
    return render_template('Google.html')

@app.route('/static', methods=['GET','POST'])
def render2():
    
    user = request.form['q']
    if user == "gmail.com":
        return render_template('gmail.html')
    elif user == "fakegmail.com":
        return render_template('gmail_hacked.html')
    else:
        return render_template('Google.html')

app.run()
    
    







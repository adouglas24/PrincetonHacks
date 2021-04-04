from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('main.html')

@app.route('/selections')
def selections():
    return render_template('selections.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True,port=5000)
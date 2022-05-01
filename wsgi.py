from flask import Flask, Response, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
load_dotenv()

USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASS")
TOKEN = os.getenv("TOKEN")

app = Flask(
    __name__,
    template_folder = "static"    
)
@app.route('/')
def login():
    return render_template("login.html")

@app.route('/auth', methods=['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    print(username, password)

    if username == USERNAME and password == PASSWORD:
        return redirect("/dashboard?token=" + TOKEN)

    return {
        "status": "fail",
        "message": "Invalid credentials"
    }

@app.route('/dashboard')
def dashboard():
    token = request.args.get('token')
    if token == TOKEN:
        return render_template("index.html")
    return redirect("/")



if __name__ == "__main__":
    app.run(debug = True)
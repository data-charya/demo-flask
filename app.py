from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def demo(data="HELLO WORLD"):
    return render_template('hello.html', data=data)

@app.route("/dummy")
def dummy():
    data = {'key': 'value', 'foo': 'bar'}  # Sample JSON data
    return jsonify(data)




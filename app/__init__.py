from flask import Flask

app = Flask(__name__)

@app.route("/")
def cookieclicker():
    return "<a href="/cookieclicker">Cookieclicker</a>"

def getcount():
    return "<a href="/getcount">Get count</a>"

app.run(host="0.0.0.0")
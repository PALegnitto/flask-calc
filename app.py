from flask import Flask, request
from operations import add


app = Flask(__name__)

@app.get("/add")
def add_numbers():
    """adds a and b and returns result as body"""

    a = request.args["a"]
    b = request.args["b"]
    return f"<body>{add(a,b)}</body>" 


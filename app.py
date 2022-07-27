from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add")
def add_numbers():
    """adds a and b and returns result as body"""

    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    return f"<body>{add(int(a),int(b))}</body>" 

@app.get("/sub")
def sub_numbers():
    """subtract a and b and returns result as body"""

    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    return f"<body>{sub(int(a),int(b))}</body>" 

@app.get("/mult")
def mult_numbers():
    """multiply a and b and returns result as body"""

    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    return f"<body>{mult(int(a),int(b))}</body>" 

@app.get("/div")
def div_numbers():
    """divides a and b and returns result as body"""

    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    return f"<body>{div(int(a),int(b))}</body>" 
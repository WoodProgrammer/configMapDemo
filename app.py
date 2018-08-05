from flask import Flask 
import os 

app = Flask(__name__)


@app.route("/v1/index")
def index():
    env1 = os.getenv("API_KEY")
    env2 = os.getenv("HEAP_SIZE")
    return env1 + env2 

@app.route("/v1"):
def doc():
    return "{'/v1/index'}"


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")


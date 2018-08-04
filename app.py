from flask import Flask 
import os 

app = Flask(__name__)


@app.route("/")
def index():
    env1 = os.getenv("API_KEY")
    env2 = os.getenv("HEAP_SIZE")
    return env1 + env2 



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")


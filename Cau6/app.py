from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return "Hello!. This is Final Lap Devnet associate!!!"
if __name__=="__main__":
 app.run(host="0.0.0.0")

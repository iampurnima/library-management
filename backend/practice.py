from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"


from classindex import Book
    

if __name__ == "__main__":
    app.run()
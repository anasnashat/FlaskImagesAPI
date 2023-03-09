from flask import Flask

app = Flask(__name__)

# genarte secret key
app.secret_key = "54fasdf5484fsdf5asdf874fasd"

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

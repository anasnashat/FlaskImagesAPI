from flask import Flask
from filters import bp as filters_pb
from action import bp as action_pb
from android import bp as android_pb


app = Flask(__name__)

# genarte secret key
app.secret_key = "54fasdf5484fsdf5asdf874fasd"

app.register_blueprint(filters_pb)
app.register_blueprint(action_pb)
app.register_blueprint(android_pb)

if __name__ == '__main__':
    app.run()

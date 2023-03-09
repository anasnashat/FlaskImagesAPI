from flask import Flask, request, jsonify, send_from_directory
from filters import bp as filters_pb
from action import bp as action_pb
from android import bp as android_pb
from helpers import allowed_extension, get_secure_filename_filepath

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSION = ['png', 'jpg', 'jpeg']

app.secret_key = "54fasdf5484fsdf5asdf874fasd"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSION'] = ALLOWED_EXTENSION

app.register_blueprint(filters_pb)
app.register_blueprint(action_pb)
app.register_blueprint(android_pb)


@app.route('/images', methods=['POST'])
def upload_images():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'no file was selected'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"Error": "No File Was Selected"}), 400

        if not allowed_extension(file.filename):
            return jsonify({'error': 'the extension not supported'}), 400

        filename, filepath = get_secure_filename_filepath(file.filename)

        file.save(filepath)

        return jsonify({
            'success': 'file uploaded successfully',
            'filename': filename
        }), 201


@app.route('/download/<name>', methods=['GET'])
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)


if __name__ == '__main__':
    app.run()

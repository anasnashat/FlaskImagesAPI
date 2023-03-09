import shutil
from datetime import datetime
import os.path
from zipfile import ZipFile

from PIL import Image
from flask import Blueprint, request, redirect, url_for, jsonify, current_app

from helpers import get_secure_filename_filepath

bp = Blueprint('android', __name__, url_prefix='/android')
ICON_SIZE = [29, 40, 57, 58, 60, 72, 76, 80, 87, 120, 152, 167, 180, 1024]


@bp.route('/', methods=['POST'])
def create_images():
    filename = request.json['filename']
    filename, filepath = get_secure_filename_filepath(filename)
    tempfolder = os.path.join(current_app.config["UPLOAD_FOLDER"], 'temp')
    os.mkdir(tempfolder)

    for size in ICON_SIZE:
        outfile=os.path.join(tempfolder,f"{size}.png")
        image = Image.open(filepath)
        image.resize((size, size)).save(outfile, "PNG")

    now = datetime.now()
    timestamp = str(datetime.timestamp(now)).rsplit('.')[0]
    zipfilename = f"{timestamp}.zip"
    zipfilepath = os.path.join(current_app.config["UPLOAD_FOLDER"], zipfilename)


    with ZipFile(zipfilepath, 'w') as zipObj:
        for foldername, subfolders, filenames in os.walk(tempfolder):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                zipObj.write(filepath, filename)
        shutil.rmtree(foldername)
        return redirect(url_for('download_file', name=zipfilename))



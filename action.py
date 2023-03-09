from flask import Blueprint, request, redirect, url_for, jsonify
from helpers import get_secure_filename_filepath
from PIL import Image

bp = Blueprint('action', __name__, url_prefix='/actions')


@bp.route('/resize', methods=['POST'])
def resize():
    filename = request.json['filename']
    filename, filepath = get_secure_filename_filepath(filename)
    try:
        width, height = int(request.json['width']), int(request.json['height'])
        out = Image.open(filepath)
        out.resize((width, height)).save(filepath)

        return redirect(url_for('download_file', name=filename))

    except FileNotFoundError:

        return jsonify({'error': 'File not found'}), 404


@bp.route('presets/<preset>', methods=['POST'])
def resize_presets(preset):
    presets = {"small": (640, 480), "medium": (1280, 960), "large": (1600, 1200)}

    if preset not in presets:
        return jsonify({'error': 'Preset not found'}), 404

    filename = request.json['filename']
    filename, filepath = get_secure_filename_filepath(filename)

    try:
        size = presets[preset]
        out = Image.open(filepath)
        out.resize(size).save(filepath)
        return redirect(url_for('download_file', name=filename))
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404


@bp.route('/rotate', methods=['POST'])
def rotate():
    filename = request.json['filename']
    filename, filepath = get_secure_filename_filepath(filename)
    try:
        degree = float(request.json['degree'])
        out = Image.open(filepath)
        out.rotate(degree).save(filepath)

        return redirect(url_for('download_file', name=filename))

    except FileNotFoundError:

        return jsonify({'error': 'File not found'}), 404


@bp.route('/flip', methods=["POST"])
def flip():
    filename = request.json['filename']
    filename, filepath = get_secure_filename_filepath(filename)

    try:
        img = Image.open(filepath)
        out = None
        if request.json['direction'] == 'horizontal':
            out = img.transpose(Image.FLIP_TOP_BOTTOM)
            print(filepath)
        else:
            out = img.transpose(Image.FLIP_LEFT_RIGHT)
        out.save(filepath)

        return redirect(url_for('download_file', name=filename))
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

from flask import Blueprint

bp = Blueprint('action', __name__, url_prefix='/actions')

@bp.route('/resize', methods=['POST'])
def resize():
    pass

@bp.route('presets/<presets>', methods=['POST'])
def resize_presets(presets):
    pass


@bp.route('/rotate', methods=['POST'])
def rotate():
    pass

@bp.route('/flip', methods=["POST"])
def flip():
    pass

from flask import Blueprint, current_app, send_from_directory

images_bp = Blueprint("images", __name__)


@images_bp.route("/images/<path:filename>", methods=["GET"])
def serve_image(filename):
    return send_from_directory(
        current_app.static_folder + "/images",
        filename
    )
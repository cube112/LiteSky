# 2026/11/01 Written by _Zeroverse
# File upload service module

from flask import Blueprint, request

from ...utils.files import is_valid_file_extension

file_upload_bp = Blueprint("file_upload", __name__, url_prefix="/service")


@file_upload_bp.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files.get("file")
    # Check if a file was uploaded
    if not uploaded_file:
        return {"message": "No file provided"}, 400

    # Check if the filename is null
    if not uploaded_file.filename:
        return {"message": "Filename is empty"}, 400

    # Check if the file extension is valid
    if not is_valid_file_extension(uploaded_file.filename):
        return {"message": "Invalid file extension"}, 400

    return {"message": "File uploaded successfully"}, 200

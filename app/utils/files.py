# 2026/11/01 Written by _Zeroverse
# File utility functions module

from flask import current_app


def get_file_extension(filename: str) -> str:
    return filename.split(".")[-1] if "." in filename else ""


def is_valid_file_extension(filename: str) -> bool:
    allowed_extensions = current_app.config.get("ALLOWED_EXTENSIONS", [])
    return get_file_extension(filename).lower() in allowed_extensions

# Written by _Zeroverse
# Identify service module
from flask import Blueprint, request
from werkzeug.security import check_password_hash

from ...exts import db
from ...models import Users

identify_bp = Blueprint("identify", __name__, url_prefix="/service")


# Check input if is valid
def is_valid_input(account, password):
    if not account:
        return False, "Account not provided"
    if not password:
        return False, "Password not provided"
    return True, ""


# Rinse account name
def rinse_account_name(account):
    return account.strip() if account else account


@identify_bp.route("/identify", methods=["POST"])
def identify():
    """
    Identify the identity of the user.
    """
    # Get the account information from the request form
    account = rinse_account_name(request.form.get("account"))
    password = request.form.get("password")

    # Validate the input
    is_valid, message = is_valid_input(account, password)
    if not is_valid:
        return {"message": message}, 400

    # refer database to check if the account and password are correct
    if "@" in account:
        user = db.session.execute(
            db.select(Users).filter_by(email=account)
        ).scalar_one_or_none()
    else:
        user = db.session.execute(
            db.select(Users).filter_by(username=account)
        ).scalar_one_or_none()

    if not user or not check_password_hash(user.password, password):
        return {"message": "Invalid account or password"}, 401

    return {"message": "User identified successfully"}, 200

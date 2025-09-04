# as rotas chamam o model


from flask import Blueprint, jsonify, request
import models.users.models as user_model
from controllers.users.validators.validator import validate_user
import json


bp = Blueprint("user", __name__)


@bp.route("/users", methods=["GET"])
def list_users():
    users = user_model.get_all_users()
    return jsonify(users)


@bp.route("/user", methods=["POST"])
def add_user():
    raw_data = request.json
    validated_data, status = validate_user(raw_data)
    data = json.loads(validated_data.data.decode("utf-8"))
    if "error" in data:
        return validated_data
    else:
        new_user = user_model.create_user(
            data["username"], data["email"], data["cpf"], data["password"]
        )
        return jsonify({"message": "Usuário criado com sucesso"}, new_user), 201

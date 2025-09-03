# as rotas chamam o model


from flask import Blueprint, jsonify, request
import models.user_model as user_model


bp = Blueprint("user", __name__)


@bp.route("/users", methods=["GET"])
def list_users():
    users = user_model.get_all_users()
    return jsonify(users)


@bp.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user_model.create_user(
        data["username"], data["email"], data["cpf"], data["password"]
    )
    return jsonify({"message": "Usuário criado com sucesso"}), 201

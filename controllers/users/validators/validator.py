from flask import jsonify
from controllers.users.exceptions.exceptions import ValidationError
import controllers.users.validators.validations as user_validator


def validate_user(raw_data):
    try:
        raw_username = raw_data.get("username")
        validated_username = user_validator.validate_username(raw_username)

        raw_email = raw_data.get("email")
        validated_email = user_validator.validate_email(raw_email)

        raw_cpf = raw_data.get("cpf")
        validated_cpf = user_validator.validate_cpf(raw_cpf)

        raw_password = raw_data.get("password")
        validated_password = user_validator.validate_password(raw_password)

        cleaned_data = {
            "username": validated_username,
            "email": validated_email,
            "cpf": validated_cpf,
            "password": validated_password,
        }
        return jsonify(cleaned_data), 200

    except ValidationError as e:
        return jsonify({
            "error": str(e),
            # "code": getattr(e, "error_code", "VALIDATION_ERROR")
        }), getattr(e, "status_code", 400)

    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500

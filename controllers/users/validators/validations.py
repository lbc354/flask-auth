import controllers.users.exceptions.exceptions as exceptions
import models.users.models as models
import re
import bcrypt


def validate_username(username):
    if not username:
        raise exceptions.UsernameMissingError()

    if len(username) > 50:
        raise exceptions.UsernameLengthError()

    existing_user = models.get_user_by_username(username)
    if existing_user:
        raise exceptions.UsernameAlreadyExistsError()

    return username.lower()


def validate_email(email):
    if not email:
        raise exceptions.EmailMissingError()

    if len(email) > 100:
        raise exceptions.EmailLengthError()

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email) is None:
        raise exceptions.EmailInvalidFormatError()

    existing_email = models.get_user_by_email(email)
    if existing_email:
        raise exceptions.EmailAlreadyExistsError()

    # Mostrar os 3 primeiros caracteres e mascarar o restante antes do @

    local, domain = email.split("@")
    if len(local) <= 3:
        masked_local = local[0] + "*" * (len(local) - 1)
    else:
        masked_local = local[:3] + "*" * (len(local) - 3)
    return masked_local + "@" + domain


def validate_cpf(cpf):
    if not cpf:
        raise exceptions.CpfMissingError()

    # Converte para string (se vier como int, float, etc.)
    cpf = str(cpf)

    # Remove caracteres não numéricos (caso venha formatado)
    cpf = re.sub(r"\D", "", cpf)

    if not cpf.isdigit():
        raise exceptions.CpfValueTypeError()

    if not len(cpf) == 11:
        raise exceptions.CpfLengthError()

    existing_cpf = models.get_user_by_cpf(cpf)
    if existing_cpf:
        raise exceptions.CpfAlreadyExistsError()

    return cpf[:3] + "*" * 8


def validate_password(password):
    if not password:
        raise exceptions.PasswordMissingError()

    if len(password) < 6:
        raise exceptions.PasswordLengthError()

    # Verifica se contém pelo menos uma letra maiúscula
    if not re.search(r"[A-Z]", password):
        raise exceptions.PasswordWeakError()

    # Verifica se contém pelo menos uma letra minúscula
    if not re.search(r"[a-z]", password):
        raise exceptions.PasswordWeakError()

    # Verifica se contém pelo menos um número
    if not re.search(r"\d", password):
        raise exceptions.PasswordWeakError()

    # Verifica se contém pelo menos um caractere especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]\\\/]', password):
        raise exceptions.PasswordWeakError()

    # Gera o hash da senha
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Retorna a senha com hash (como bytes ou como string, dependendo da sua necessidade)
    return hashed_password.decode("utf-8")

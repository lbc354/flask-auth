# superclasse
class ValidationError(ValueError):
    status_code = 400
    # error_code = "VALIDATION_ERROR"
    default_message = "Validation error"

    def __init__(self, message=None):
        super().__init__(message or self.default_message)


# não enviou username pelo formulário
class UsernameMissingError(ValidationError):
    status_code = 400
    # error_code = "USERNAME_MISSING"
    default_message = "Username is required."


# username ultrapassou limite de caracteres
class UsernameLengthError(ValidationError):
    status_code = 400
    default_message = "Too long (max: 50)."


# username já existe no banco
class UsernameAlreadyExistsError(ValidationError):
    status_code = 409
    default_message = "Username already exists."


# não enviou email pelo formulário
class EmailMissingError(ValidationError):
    status_code = 400
    default_message = "Email is required."


# email ultrapassou limite de caracteres
class EmailLengthError(ValidationError):
    status_code = 400
    default_message = "Too long (max: 100)."


# email com formato inválido (diferente de a@a.a)
class EmailInvalidFormatError(ValidationError):
    status_code = 400
    default_message = "Invalid format value."


# email já existe no banco
class EmailAlreadyExistsError(ValidationError):
    status_code = 409
    default_message = "Email already exists."


# não enviou cpf pelo formulário
class CpfMissingError(ValidationError):
    status_code = 400
    default_message = "CPF is required."


# cpf não é apenas números
class CpfValueTypeError(ValidationError):
    status_code = 400
    default_message = "CPF must contain only numbers."


# cpf ultrapassou limite de caracteres
class CpfLengthError(ValidationError):
    status_code = 400
    default_message = "Invalid length (must be 11)."


# cpf já existe no banco
class CpfAlreadyExistsError(ValidationError):
    status_code = 409
    default_message = "CPF already exists."


# não enviou password pelo formulário
class PasswordMissingError(ValidationError):
    status_code = 400
    default_message = "Password is required."


# password ultrapassou limite de caracteres
class PasswordLengthError(ValidationError):
    status_code = 400
    default_message = "Too short (min: 6)."


# password não atende ao padrão de segurança
class PasswordWeakError(ValidationError):
    status_code = 400
    default_message = (
        "Password must have uppercase and lowercase letters, "
        "a number, and a special character."
    )

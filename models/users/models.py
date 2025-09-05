# aqui ficam as queries sql relacionadas a usuários


from config.db import get_db_connection


def mask_email(email):
    if not email or "@" not in email:
        return ""
    # Mostrar os 3 primeiros caracteres e mascarar o restante antes do @
    local, domain = email.split("@", 1)
    if len(local) <= 3:
        masked_local = local[0] + "*" * (len(local) - 1) if len(local) > 0 else ""
    else:
        masked_local = local[:3] + "*" * (len(local) - 3)
    return masked_local + "@" + domain


def mask_cpf(cpf):
    if not cpf or len(cpf) < 3:
        return ""
    # Mostrar os 3 primeiros caracteres e mascarar o restante
    return cpf[:3] + "*" * 8


def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # retorna dict em vez de tupla
    cursor.execute("SELECT id, username, email, cpf FROM user")
    users = cursor.fetchall()
    for user in users:
        user["email"] = mask_email(user["email"])
        user["cpf"] = mask_cpf(user["cpf"])
    conn.close()
    return users


def get_user_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # retorna dict em vez de tupla
    cursor.execute("SELECT id, username, email, cpf FROM user WHERE id = %s", (id,))
    user = cursor.fetchone()
    user["email"] = mask_email(user["email"])
    user["cpf"] = mask_cpf(user["cpf"])
    conn.close()
    return user


def get_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # retorna dict em vez de tupla
    cursor.execute(
        "SELECT id, username, email, cpf FROM user WHERE username = %s", (username,)
    )
    user = cursor.fetchone()
    conn.close()
    return user


def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # retorna dict em vez de tupla
    cursor.execute(
        "SELECT id, username, email, cpf FROM user WHERE email = %s", (email,)
    )
    user = cursor.fetchone()
    conn.close()
    return user


def get_user_by_cpf(cpf):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # retorna dict em vez de tupla
    cursor.execute("SELECT id, username, email, cpf FROM user WHERE cpf = %s", (cpf,))
    user = cursor.fetchone()
    conn.close()
    return user


def create_user(username, email, cpf, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # cria
    cursor.execute(
        "INSERT INTO user (username, email, cpf, password) VALUES (%s, %s, %s, %s)",
        (username, email, cpf, password),
    )
    conn.commit()

    # pega o ID do novo usuário
    new_user_id = cursor.lastrowid

    # busca o usuário recém-criado
    cursor.execute("SELECT id FROM user WHERE id = %s", (new_user_id,))
    new_user = cursor.fetchone()

    conn.close()
    return new_user

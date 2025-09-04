# aqui ficam as queries sql relacionadas a usuários


from config.db import get_db_connection


def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # retorna dict em vez de tupla
    cursor.execute("SELECT id, username, email, cpf FROM user")
    users = cursor.fetchall()
    conn.close()
    return users


def get_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # retorna dict em vez de tupla
    cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
    user = cursor.fetchone()
    conn.close()
    return user


def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # retorna dict em vez de tupla
    cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
    user = cursor.fetchone()
    conn.close()
    return user


def get_user_by_cpf(cpf):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # retorna dict em vez de tupla
    cursor.execute("SELECT * FROM user WHERE cpf = %s", (cpf,))
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
    cursor.execute(
        "SELECT id, username, email, cpf, created, updated FROM user WHERE id = %s",
        (new_user_id,),
    )
    new_user = cursor.fetchone()

    conn.close()
    return new_user

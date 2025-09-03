# aqui ficam as queries sql relacionadas a usuários


from config.db import get_db_connection


def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # retorna dict em vez de tupla
    cursor.execute("SELECT id, username, email, cpf FROM user")
    users = cursor.fetchall()
    conn.close()
    return users


def create_user(username, email, cpf, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user (username, email, cpf, password) VALUES (%s, %s, %s, %s)",
        (username, email, cpf, password),
    )
    conn.commit()
    conn.close()

from flask import Flask
from dynaconf import FlaskDynaconf
from config.db import get_db_connection
from controllers.users import controllers


app = Flask(__name__)


# Carregar Dynaconf no Flask
FlaskDynaconf(app, settings_files=["config/settings.toml", "config/.secrets.toml"])


@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT NOW()")  # horário do banco
    result = cursor.fetchone()
    conn.close()
    return f"Hora no banco: {result[0]}"


app.register_blueprint(controllers.bp)

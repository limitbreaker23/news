from flask import app
from website import create_app

app = create_app()

app.run(host='0.0.0.0', port=8080)
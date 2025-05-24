from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from backend.blueprints.autor_blueprint import autor_blueprint
from backend.blueprints.genero_blueprint import genero_blueprint
from backend.blueprints.libro_blueprint import libro_blueprint
from backend.blueprints.user_blueprint import user_blueprint

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
CORS(app)

jwt = JWTManager(app)

app.register_blueprint(autor_blueprint)
app.register_blueprint(genero_blueprint)
app.register_blueprint(libro_blueprint)
app.register_blueprint(user_blueprint)

@app.route('/')
def home():
    return {"message": "API Flask funcionando correctamente"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
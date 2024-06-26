#!/usr/bin/python3

'''
    quick doc
'''

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from werkzeug.security import check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "SweetHomeAlabama1234"
jwt = JWTManager(app)

users = {
      "user1": {
          "username": "user1",
          "password":  # "Colombia"
          "scrypt:32768:8:1$H8LLOa8s8dRzTfa7$5a4ace93a9fa5a9c609b3ba4f43c10d05\
cdbc4116ba3c21efeca0cabafaca7a54f31e0bfde1616e1eb35be02db5b1b67fd2465c75855a6c\
ae22172c717779d8b",
          "role": "user"
          },
      "admin1": {
          "username": "admin1",
          "password":  # "Venezuela"
          "scrypt:32768:8:1$End4HJiKMTJMe5kc$be02de334c13dacf9d3c7f4ef59bfca06\
cc87bb9f8f9dd4856b44b45135bdcef859e7c15fb6bfd15e98aa0a4e10b8fa87183cdbe244b3af\
ffad9fc210094f967",
          "role": "admin"
          }
  }
tokens = {}


@auth.error_handler
def handle_basic(err):
    return {"error": "401 Unauthorized"}, 401


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return username


@app.route('/basic-protected')
@auth.login_required
def index():
    return {"message": "Basic Auth: Access Granted"}, 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "401 Unauthorized"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "401 Unauthorized"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "401 Unauthorized"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "401 Unauthorized"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "401 Unauthorized"}), 401


@app.post('/login')
def login():
    dic = request.get_json()
    if "username" not in dic or "password" not in dic:
        return {"error": "Invalid credentials."}, 401
    username = dic["username"]
    if username in users:
        if "password" not in users[username]:
            return {"error": "Needs Password"}
        if check_password_hash(dic["password"],
                               users[username]["password"]):
            role = users[username]["role"]
            access_token = create_access_token(
                identity=username,
                additional_headers={"role": role}
                )
            tokens[username] = access_token
            return {"access_token": access_token}, 200
    return {"error": "Invalid credentials."}, 401


@app.get('/jwt-protected')
@jwt_required()
def jwt():
    return "JWT Auth: Access Granted", 200


@app.get('/admin-only')
@jwt_required()
def admin():
    jwt = get_jwt()
    role = jwt["role"]
    if role != "admin":
        return {"error": "403 Forbidden"}, 403
    return "Admin Access: Granted", 200


if __name__ == '__main__':
    app.run()

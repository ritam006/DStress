from flask import request, jsonify, Response, current_app
from ..models import model_user

def add_new_user():
    if request.method == 'POST':
        kwags = request.get_json(force=True)
        username = kwags.get('username')
        password = kwags.get('password')
        response = model_user.User.add_new_user(username, password)
        if response is None:
            return Response(status=400)
        return jsonify(response)

def login():
    if request.method == 'PUT':
        kwags = request.get_json(force=True)
        username = kwags.get('username')
        password = kwags.get('password')
        response = model_user.User.login(username, password)
        if response is None:
            return Response(status=400)
        return jsonify(response)

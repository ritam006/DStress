from flask import request, jsonify, Response, current_app
from ..models import model_user, model_home

def get_feed():
    if request.method == 'GET':
        response = model_home.get_feed()
        if response is None:
            return Response(status=400)
        return jsonify(response)

def sentiment():
    if request.method == 'POST':
        kwags = request.get_json(force=True)
        response = model_home.sentiment(kwags['text'])
        if response is None:
            return Response(status=400)
        return jsonify(response)

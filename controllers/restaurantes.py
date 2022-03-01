from flask import Flask 
from flask_restx import Api, Resource


from src.server.instance import server

app = server.app
api = server.api

restaurantes = [
    {'codigo': 0, 'restaurante': 'Coco Bambu'}
]

@api.route('/restaurante')
class Restaurantes (Resource):
    def get(self, ):
        return restaurantes


    def post(self, ):
        response = api.payload
        restaurantes.append(response)
        return response, 200




from flask import Flask, render_template
from flask_restx import Api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='Restaurantes',
            description='APi simples de restaurante',
            doc='/docs'
        )
        
    def run(self,):
        self.app.run(
            debug=True
        )

server = Server()
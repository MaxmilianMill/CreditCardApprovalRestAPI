from flask import Flask
from flask_restful import Api
from app.classifier import PredictorModel

app = Flask(__name__)
api = Api(app)

api.add_resource(PredictorModel, '/api/predict')


if __name__ == '__main__':
    app.run(debug=True)

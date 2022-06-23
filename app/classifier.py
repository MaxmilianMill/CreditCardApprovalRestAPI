from flask import request, jsonify
from flask_restful import Resource
import pickle
import numpy as np
from app.validator import Validator
import logging as log


class PredictorModel(Resource):
    model = pickle.load(open('app/model/credit_approval_knn_model.pkl', 'rb'))
    scaler = pickle.load(open('app/model/scaler_knn_model.pkl', 'rb'))

    def get(self):

        try:
            gender = int(request.args.get('gender'))
            reality = int(request.args.get('realty'))
            count_children = int(request.args.get('children'))
            income_type = int(request.args.get('income_type'))
            family_status = int(request.args.get('family_status'))
            time_employed = float(request.args.get('time_employed'))
            email = int(request.args.get('email'))
            family_members = int(request.args.get('family'))

        except (ValueError, TypeError) as error:
            return jsonify(code='VE',
                           error='One of the parameters has a wrong value type')

        except:
            return jsonify(code='UK',
                           error='Undefined Error')

        validate = Validator(gender, reality, count_children, income_type, family_status,
                             time_employed, email, family_members)

        if validate.isValid():
            feature_values = np.asarray([gender, reality, count_children, income_type, family_status,
                                         time_employed, email, family_members])

            scaled_values = self.scaler.transform([feature_values])
            prediction = self.model.predict(scaled_values)

            if prediction[0] == 1:
                return jsonify(approved=True)
            else:
                return jsonify(approved=False)

        else:
            raise ValueError



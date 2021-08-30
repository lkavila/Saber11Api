from flask import Blueprint
#from App.Domain.PredictiveModel import predictive_model
from flask import jsonify
from App.Domain.Analysis import analytics

main = Blueprint('inicio', __name__)

@main.route('/')
def home():
    #predictive_model
    x1 = analytics.o_p_d_20191()
    x1 = x1.to_dict()
    x2 = analytics.o_p_d_20192()
    x2 = x2.to_dict()
    x3 = analytics.o_p_d_20201()
    x3 = x3.to_dict()
    x4 = analytics.o_p_d_20202()
    x4 = x4.to_dict()
    x5 = analytics.o_p_d_20211()
    x5 = x5.to_dict()

    result = {
        "puntajes 20191": x1,
        "puntajes 20192": x2,
        "puntajes 20201": x3,
        "puntajes 20202": x4,
        "puntajes 20211": x5,
    }

    return result
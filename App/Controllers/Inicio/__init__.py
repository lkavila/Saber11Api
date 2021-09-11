from flask import Blueprint
#from App.Domain.PredictiveModel import predictive_model
from flask import jsonify
from App.Domain.Analysis import analytics
from App.Domain.Analysis.mejores_colegios import mejores_colegios

main = Blueprint('inicio', __name__)

@main.route('/')
def home():
    #predictive_model
    """x1 = analytics.o_p_d_20191()
    x1 = x1.to_dict()
    x2 = analytics.o_p_d_20192()
    x2 = x2.to_dict()
    x3 = analytics.o_p_d_20201()
    x3 = x3.to_dict()
    x4 = analytics.o_p_d_20202()
    x4 = x4.to_dict()
    x5 = analytics.o_p_d_20211()
    x5 = x5.to_dict()"""

    result = {
        "Mejores colegios 20191": mejores_colegios(20192, None).to_dict(),
        #"Mejores colegios 20192": mejores_colegios(20192, None).to_dict(),
        #"Mejores colegios 20201": mejores_colegios(20201, None).to_dict(),
        #"Mejores colegios 20202": mejores_colegios(20202, None).to_dict(),
        #"Mejores colegios 20211": mejores_colegios(20211, None).to_dict(),
    }

    return result
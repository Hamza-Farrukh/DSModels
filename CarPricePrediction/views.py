from django.shortcuts import render
import pickle
import numpy as np
import sklearn

def car_price(request):
    return render(request, 'CarPricePrediction/car_price.html')

def result(request):
    year = int(request.GET.get('year'))
    year = 2022 - year
    kms_driven = int(request.GET.get('kms_driven'))
    owner = int(request.GET.get('owner'))
    fuel_type = request.GET.get('fuel')
    fuel_type_petrol = 0
    fuel_type_diesel = 0
    if fuel_type == 'p':
        fuel_type_petrol = 1
        fuel_type_diesel = 0
    else:
        fuel_type_petrol = 0
        fuel_type_diesel = 1
    transmission = request.GET.get('transmission')
    if transmission == 'm':
        transmission = 1
    else:
        transmission = 0
    seller_type = request.GET.get('seller')
    if seller_type == 'i':
        seller_type = 1
    else:
        seller_type = 0
    features = [[kms_driven, owner, fuel_type_diesel , fuel_type_petrol, seller_type, transmission, year]]
    with open("static/CarPricePrediction/model/model.pkl", "rb") as f:
        model = pickle.load(f)
    y_pred = model.predict(features)
    params = {'result':y_pred}
    return render(request, 'CarPricePrediction/car_price_result.html', params)

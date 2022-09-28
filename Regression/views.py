from django.shortcuts import render
import pickle


# Create your views here.
def regression(request):
    return render(request, 'Regression/regression.html')


def car_price(request):
    return render(request, 'Regression/CarPricePrediction/values.html')


def result(request):
    year = int(request.GET.get('year'))
    year = 2022 - year
    kms_driven = int(request.GET.get('kms_driven'))
    owner = int(request.GET.get('owner'))
    fuel_type = request.GET.get('fuel')
    if fuel_type == 'p':
        fuel_type_petrol = 1
        fuel_type_diesel = 0
        fuel_type = 'Petrol'
    elif fuel_type == 'd':
        fuel_type_petrol = 0
        fuel_type_diesel = 1
        fuel_type = 'Diesel'
    else:
        fuel_type_petrol = 0
        fuel_type_diesel = 0
        fuel_type = 'CNG'
    transmission = request.GET.get('transmission')
    if transmission == 'm':
        transmission = 1
        mode = 'Manual'
    else:
        transmission = 0
        mode = 'Automatic'
    seller_type = request.GET.get('seller')
    if seller_type == 'i':
        seller_type = 1
        seller = 'Individual'
    else:
        seller_type = 0
        seller = 'Dealer'

    features = [[kms_driven, owner, fuel_type_diesel, fuel_type_petrol, seller_type, transmission, year]]
    feature_names = [['Distance Driven', kms_driven], ['No. of Owner(s)', owner], ['Fuel Type', fuel_type],
                     ['Seller Type', seller], ['Transmission Type', mode], ['Year Built', 2022-year]]
    with open("staticfiles/Regression/CarPricePrediction/model/model.pkl", "rb") as f:
        model = pickle.load(f)
    y_pred = model.predict(features)
    accuracy = 79
    params = {'result': y_pred[0], 'accuracy': accuracy, 'features': feature_names}
    return render(request, 'Regression/CarPricePrediction/results.html', params)

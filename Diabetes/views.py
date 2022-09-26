from django.shortcuts import render
import pickle
import pandas as pd


def diabetes(request):
    return render(request, 'Diabetes/values.html')


def result(request):
    bmi = float(request.GET.get('BMI'))
    pedigree_function = float(request.GET.get('pf'))
    age = int(request.GET.get('age'))
    skinthickness = float(request.GET.get('skin'))
    glucose = float(request.GET.get('glucose'))
    insulin = float(request.GET.get('insulin'))
    bp = float(request.GET.get('bp'))
    pregnancy = int(request.GET.get('pregnant'))

    features = {'BMI': bmi, 'DiabetesPedigreeFunction': pedigree_function, 'Age': age, 'SkinThickness': skinthickness,
                'Glucose': glucose, 'Insulin': insulin, 'BloodPressure': bp, 'Pregnancies': pregnancy}
    features = pd.DataFrame(features, index=(0, 1))
    features.drop(1, axis=0)
    feature_names = [['BMI', bmi], ['Pedigree Function', pedigree_function], ['Age', age],
                     ['Skin Thickness', skinthickness], ['Glucose', glucose], ['Insulin', insulin],
                     ['Blood Pressure', bp], ['No. of Pregnancies', pregnancy]]

    with open("static/Diabetes/model/model.pkl", "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(features)
    accuracy = 75
    if y_pred[0] == 0:
        y_pred = 'No'
    else:
        y_pred = 'Yes'

    params = {'result': y_pred, 'accuracy': accuracy, 'features': feature_names}
    return render(request, 'Diabetes/results.html', params)

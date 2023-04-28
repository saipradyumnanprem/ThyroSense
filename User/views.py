from django.http import HttpResponse
from django.shortcuts import redirect, render
import joblib


import pandas as pd

model = joblib.load('./Model/thyroid_model.pkl')


def user_profile(request):
    return render(request, 'user_profile.html')


# def community(request):
#     return render(request, 'user_blog.html')


def user_dashboard(request):
    context = {"hello": "hello world"}
    return render(request, 'user_dashboard.html', context)


def user_report(request):
    user = request.user

    report = user.userreport_set.all()

    report_list = []
    for i in report.iterator():
        report_list.append(i.report_id)

    context = {'report': report, 'rep': report_list}
    return render(request, 'user_report.html', context)


def add_report(request):

    temp = {}
    if request.method == 'POST':
        user = request.user
        temp['Age'] = request.POST.get('age')
        temp['T3'] = request.POST.get('t3')
        temp['TT4'] = request.POST.get('tt4')
        temp['T4U'] = request.POST.get('t4u')
        temp['FTI'] = request.POST.get('fti')
        temp['Sex_M'] = int(request.POST.get('sex'))
        temp['Sick_t'] = int(request.POST.get('sick'))
        temp['Pregnant_t'] = int(request.POST.get('pregnant'))
        temp['Thyroid Surgery_t'] = int(request.POST.get('thyroid_surgery'))
        temp['Goitre_t'] = int(request.POST.get('goitre'))
        temp['Tumor_t'] = int(request.POST.get('tumor'))

        category = model.predict(
            [[temp['Age'], temp['T3'], temp['TT4'], temp['T4U'], temp['FTI'], temp['Sex_M'],
              temp['Sick_t'], temp['Pregnant_t'], temp['Thyroid Surgery_t'], temp['Goitre_t'], temp['Tumor_t']]])

        cat = ""

        if category[0] == 0:
            cat = "Hyperthyroid"
        elif category[0] == 1:
            cat = "Hypothyroid"
        elif category[0] == 2:
            cat = "Negative"
        elif category[0] == 3:
            cat = "Sick"

        user.userreport_set.create(age=temp['Age'], t3=temp['T3'], tt4=temp['TT4'], t4u=temp['T4U'],
                                   fti=temp['FTI'], sex=temp['Sex_M'], sick=temp['Sick_t'],
                                   pregnant=temp['Pregnant_t'], thyroid_surgery=temp['Thyroid Surgery_t'], goitre=temp['Goitre_t'], tumor=temp['Tumor_t'], category=cat)

        rep = user.userreport_set.all()

        context = {'category': category[0], 'temp': temp, 'report': rep}
        return render(request, 'user_report.html', context)

    # context = {'report': rep}
    return render(request, 'add_report.html')

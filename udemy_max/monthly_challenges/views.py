from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


months = {
    'january': 'First month',
    'february': 'Second month',
    'march': 'Third month',
    'april': 'Fourth month',
    'may': 'Fifth month',
    'june': 'Sixth month',
    'july': 'Seventh month',
    'august': 'Eighth month',
    'september': 'Ninth month',
    'october': 'Tenth month',
    'november': 'Eleventh month',
    'december': 'Twelth month'
}


def hi(request):
    return HttpResponse('Hi from django')


def month(request, month):
    try:
        return HttpResponse(f'{months[month]} => {month}')
    except:
        return HttpResponseNotFound('Invalid month')


def month_by_number(request, month):
    
    if month > 12 or month < 1:
        return HttpResponseNotFound('Invalid month input')
    
    months_list = list(months.keys())
    print(months_list)
    print("month is " + str(month))
    redirect_month = months_list[month-1]
    redirect_path = reverse("monthly-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
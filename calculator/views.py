from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
import joblib
# Create your views here.

def calculator(request):
    return render(request,'calculator/calculator.html')
def result(request):
    user = request.user
    model = joblib.load('Final_Stress_Model.sav')
    lis = []
    status = ""
    if request.method == 'POST':
        quiz1 = request.POST.get('QZ1')
        quiz2 = request.POST.get('QZ2')
        quiz3 = request.POST.get('QZ3')
        sw1 = request.POST.get('SW1')
        sw2 = request.POST.get('SW2')
        as1 = request.POST.get('AS1')
        as2 = request.POST.get('AS2')

        lis.extend([quiz1,quiz2,quiz3,sw1,sw2,as1,as2])
        
        ans = model.predict([lis])
        if ans == 1:
            status = "stress"
        else:
            status = "Not Stress"
    context = {
		'status':status,
        'user':user,
        'ans':ans
	}
    return render(request,'calculator/result.html',context)
from django.urls import path
from .views import calculator,result

urlpatterns = [
    path('calculator/', calculator, name='calculator'),
    path('calculator/result',result,name='result'),
]
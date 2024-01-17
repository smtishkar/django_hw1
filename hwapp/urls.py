from django.urls import path
import hwapp.views as views


urlpatterns = [
    path('',views.index, name='index'),
    path('about/', views.about_company, name='about'),
]
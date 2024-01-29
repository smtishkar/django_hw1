from django.urls import path
import hwapp.views as views


urlpatterns = [
    path('',views.index, name='index'),
    path('about/', views.about_company, name='about'),
    path('customers', views.customers_view, name='customers'),
    path('things', views.things_view, name='things'),
    path('orders', views.orders_view, name='orders'),
    path('customer_orders/<int:customer_id>/<int:filter_days>', views.customer_orders_view, name='customer_orders')
]
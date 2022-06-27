from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path("register",views.register,name='register'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("rent",views.rent,name='rent'),
    path("payment",views.payment,name='payment'),
    path("success",views.success,name='success'),
    path("cancel",views.cancel,name='cancel'),
    path("booking_list",views.booking_list,name="booking_list"),
    path("cancel_order",views.cancel_order,name='cancel_order')
]
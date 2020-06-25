from django.urls import path

from . import views

urlpatterns = [
    path('payjp-form', views.payjp, name='payjp'), # payjp 公式 doc
    path('payjp2', views.payjp_2, name='payjp2'), 
]
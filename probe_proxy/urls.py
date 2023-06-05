from django.urls import path
from . import views

app_name = 'probe_proxy'

urlpatterns = [
    path('', views.index, name='index'),
    path('breached/<str:email>', views.breached, name='breached'),
]

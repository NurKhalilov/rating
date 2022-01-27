from django.urls import path
from . import views

app_name = 'rate'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('report/<int:region_id>/', views.report_add, name='report_add'),
    path('table/', views.average_show, name='average_show'),
    path('json/', views.json, name='json'),
    path('graph/', views.graph_show, name='graph_show'),
]


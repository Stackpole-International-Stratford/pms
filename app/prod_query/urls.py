from django.urls import path

from . import views

urlpatterns = [
    path('', views.prod_query, name='prod-query'),
    path('test', views.weekly_summary, name='prod-summary'),
    path('weekly-prod', views.weekly_prod, name='weekly-prod'),
    path('rejects', views.reject_query, name='rejects'),
    path('cycle-times', views.cycle_times, name='cycle-times'),
    path('<str:machine>/<int:start_timestamp>/<int:times>/',
         views.machine_detail, name='machine_detail'),
]

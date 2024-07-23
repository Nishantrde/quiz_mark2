from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('lrbd', leaderboard),
    path('teams', team_list, name='team_list'),
    path('r1', round1),
    path('s', suffel),
    path('mkt', make_teams),
    path('mkq', make_quest),
    path('mkl', mk_list),
]


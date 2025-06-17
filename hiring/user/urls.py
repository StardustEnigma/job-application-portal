from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('ChangePassword/',views.password_change_view,name='passwordChange')
]

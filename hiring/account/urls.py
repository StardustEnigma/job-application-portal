from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('activate/<str:uidb64>/<str:token>/',views.activate_account,name='activate')

]

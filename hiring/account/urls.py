from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('activate/<str:uidb64>/<str:token>/',views.activate_account,name='activate'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout')

]

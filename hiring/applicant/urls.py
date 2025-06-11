from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('application/',views.application,name='application'),
    path('application/success/<int:pk>/',views.application_success,name='application_success')
]

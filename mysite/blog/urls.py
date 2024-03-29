from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('register/', views.register,name='register'),
    path("logout/", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
]

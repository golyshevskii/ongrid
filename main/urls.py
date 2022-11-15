from django.urls import path
from django.contrib.auth import views
from .views import main_page


urlpatterns = [
    path('', main_page, name='mainpage'),
    path('login/', views.LoginView.as_view(template_name='base.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='base.html'), name='logout'),
]
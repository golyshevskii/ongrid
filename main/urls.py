from django.urls import path
from django.contrib.auth import views
from .views import main_page, login_page, signup_page, logout_page


urlpatterns = [
    path('', main_page, name='mainpage'),
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('logout/', logout_page, name='logout'),
]
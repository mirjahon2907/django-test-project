from django.contrib import admin
from django.urls import include, path
from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('account/', account, name='account'),
    path('single-project/', single_project, name='single-project'),
    path('forget_password/', forget_password, name='forget_password'),
    path('profiles/<int:pk>', profile_detail, name='profile_detail'),

]
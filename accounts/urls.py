from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user/', views.user, name='user'),
    path('profile/<username>', views.profile, name='profile'),

    #kakao 
    path('kakao_login/', views.kakao_login, name='kakao_login'),
]

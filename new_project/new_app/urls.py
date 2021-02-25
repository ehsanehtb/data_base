from django.urls import path
from new_app import views

app_name = 'new_app'

urlpatterns = [
    path('registere/',views.registere,name='registere'),
    path('user_login/',views.user_login,name='user_login'),
]

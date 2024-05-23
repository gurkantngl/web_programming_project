from django.contrib import admin
from django.urls import path
from .presentation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('add-session/', views.add_session_data, name='add_session_data'),
    path('read-session/', views.read_session_data, name='read_session_data'),
    path('add-cookie/', views.add_cookie, name='add_cookie'),
    path('read-cookie/', views.read_cookie, name='read_cookie'),
]

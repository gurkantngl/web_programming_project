from django.contrib import admin
from django.urls import path
from .presentation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
<<<<<<< HEAD
]
=======
]
>>>>>>> master

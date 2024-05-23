# business/services.py
from django.contrib.auth.hashers import make_password, check_password
from .models import User

class UserService:
    @staticmethod
    def register_user(form):
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            return user
        return None

    @staticmethod
    def authenticate_user(email, password):
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return user
        except User.DoesNotExist:
            return None
        return None

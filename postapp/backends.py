from django.contrib.auth.backends import BaseBackend
from postapp.models import CustomUser

class EmailBackend(BaseBackend):
    def authenticate(self, request, username = ..., password = ..., **kwargs):
        try:
            user_obj=CustomUser.objects.get(email=username)
            user_password=user_obj.password

            if user_obj.check_password(password):
                return user_obj
            else:
                return None
        except:
            return None

    def get_user(self, user_id):
        return CustomUser.objects.get(id=user_id)
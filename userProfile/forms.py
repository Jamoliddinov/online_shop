from django.contrib.auth import get_user_model
from django.forms import ModelForm
from userProfile.models import Profile

UserModel = get_user_model()


class RegisterForm(ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'username',
            'password',
        ]

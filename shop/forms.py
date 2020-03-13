from django.contrib.auth import get_user_model
from django.forms import ModelForm, Form, forms, fields

UserModel = get_user_model()


class UserLoginForm(Form):
    username = fields.CharField(max_length=50, required=True)
    password = fields.CharField(max_length=50, required=True)
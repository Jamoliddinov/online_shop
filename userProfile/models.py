from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    img = models.ImageField(null=True)
    address = models.CharField(max_length=255)

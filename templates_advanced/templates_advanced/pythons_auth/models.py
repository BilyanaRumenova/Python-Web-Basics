from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class PythonsUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
    )

    USERNAME_FIELD = 'email'


from django.db import models

import uuid

def hex_code():
    return uuid.uuid4().hex



class GenderTextChoies(models.TextChoices):
    MALE = 'Male'
    FEMALE = 'Female'
from django.db import models

class BaseModel(models.Model):
    created_data = models.DateTimeField()
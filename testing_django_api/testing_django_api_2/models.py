from django.db import models

# Create your models here.
class drinks(models.Model):
    username = models.CharField(default="", max_length=50)
    Age = models.IntegerField()

    def __str__(self) -> str:
        return self.username

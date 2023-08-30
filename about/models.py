from django.db import models


class Feedback(models.Model):
    full_name = models.CharField(max_length=222)
    avatar = models.ImageField(upload_to='feedback/')
    position = models.CharField(max_length=222)
    message = models.TextField()

    def __str__(self):
        return self.full_name

from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.URLField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.description + self.image
    
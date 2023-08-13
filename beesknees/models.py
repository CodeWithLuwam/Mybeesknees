from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.URLField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()


class Entry(models.Model): 
    date=models.CharField(max_length=20)
    sets=models.CharField(max_length=20)
    reps_or_mins=models.CharField(max_length=20) 
    user=models.ForeignKey(User, on_delete=models.CASCADE,  related_name="entries") #null=True,)
    exercise=models.ForeignKey(Exercise, on_delete=models.CASCADE)
    # User.objects.filter(article__pk=1)



# routes


def __str__(self):
    return self.name + ' ' + self.description + self.image

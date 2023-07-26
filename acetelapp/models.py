from django.db import models

# Create your models here.
class Course(models.Model):
    image =models.ImageField(upload_to = 'images')
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=225)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()

    def __str__(self):
        return self.title


class Exam(models.Model):
    image =models.ImageField(upload_to = 'images')
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=225)
    amount = models.IntegerField()
    question = models.IntegerField()

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)  # Backend, Frontend, DevOps, ML

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree

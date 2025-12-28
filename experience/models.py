from django.db import models

# Create your models here.

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.role} - {self.company}"


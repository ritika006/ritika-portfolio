from django.db import models

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    tech_stack = models.ManyToManyField(Technology)
    github_link = models.URLField()
    live_link = models.URLField(blank=True)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateField()

    def __str__(self):
        return self.title


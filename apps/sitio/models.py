from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Projecto'
        verbose_name_plural = 'Projectos'


class Task(models.Model):
    title = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=False, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.project.title

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

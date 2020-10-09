from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    author = models.ManyToManyField(Author)
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    release_date = models.DateField()

    def __str__(self):
        return self.title


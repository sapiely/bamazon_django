from django.db import models
from django.core.exceptions import ValidationError


class Author(models.Model):
    full_name = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name

    def clean(self, *args, **kwargs):
        # run the base validation
        super(Author, self).clean(*args, **kwargs)

        # Don't allow dates earlier than birth date.
        if self.birth_date > self.death_date :
            raise ValidationError('Death time must be later birth date.')


class Book(models.Model):
    author = models.ManyToManyField(Author, related_name='author')
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    release_date = models.DateField()

    def __str__(self):
        return self.title

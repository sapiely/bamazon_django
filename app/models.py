from django.db import models
from django.core.exceptions import ValidationError
import os, uuid
from django_resized import ResizedImageField


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("images", filename)


class Author(models.Model):
    full_name = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    photo = ResizedImageField(
        size=[500, 500], quality=100, upload_to=get_file_path, blank=True
    )

    def __str__(self):
        return self.full_name

    def clean(self, *args, **kwargs):
        # run the base validation
        super(Author, self).clean(*args, **kwargs)

        # Don't allow dates earlier than birth date.
        if not self.death_date:
            return
        if self.birth_date > self.death_date:
            raise ValidationError("Death time must be later birth date.")


class Book(models.Model):
    author = models.ManyToManyField(Author, related_name="author")
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    release_date = models.DateField()
    photo = ResizedImageField(
        size=[500, 500], quality=100, upload_to=get_file_path, blank=True
    )

    def __str__(self):
        return self.title

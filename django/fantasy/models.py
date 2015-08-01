
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Author(models.Model):
    name = models.CharField(max_length=80)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True)


class Series(models.Model):
    title = models.CharField(max_length=80)
    photo = GenericRelation(
        'fantasy.Photo',
        content_type_field='imageable_type',
        object_id_field='imageable_id',
    )


class Book(models.Model):
    series = models.ForeignKey('fantasy.Series', null=True)
    author = models.ForeignKey('fantasy.Author')
    title = models.CharField(max_length=80)
    date_published = models.DateField()


class Chapter(models.Model):
    title = models.CharField(max_length=80)
    book = models.ForeignKey('fantasy.Book')
    ordering = models.PositiveIntegerField()

    class Meta:
        unique_together = (
            ('book', 'ordering'),
        )


class Store(models.Model):
    name = models.CharField(max_length=80)
    books = models.ManyToManyField('fantasy.Book')


class Photo(models.Model):
    title = models.CharField(max_length=80)
    uri = models.URLField()

    imageable_type = models.ForeignKey(ContentType)
    imageable_id = models.PositiveIntegerField()
    imageable_object = GenericForeignKey('imageable_type', 'imageable_id')

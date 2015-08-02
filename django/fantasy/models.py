
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(TimestampedModel):
    name = models.CharField(max_length=80)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True)


class Series(TimestampedModel):
    title = models.CharField(max_length=80)
    photo = GenericRelation(
        'fantasy.Photo',
        content_type_field='imageable_type',
        object_id_field='imageable_id',
    )


class Book(TimestampedModel):
    series = models.ForeignKey('fantasy.Series', null=True)
    author = models.ForeignKey('fantasy.Author')
    title = models.CharField(max_length=80)
    date_published = models.DateField()


class Chapter(TimestampedModel):
    title = models.CharField(max_length=80)
    book = models.ForeignKey('fantasy.Book')
    ordering = models.PositiveIntegerField()

    class Meta:
        unique_together = (
            ('book', 'ordering'),
        )


class Store(TimestampedModel):
    name = models.CharField(max_length=80)
    books = models.ManyToManyField('fantasy.Book')


class Photo(TimestampedModel):
    title = models.CharField(max_length=80)
    uri = models.URLField()

    imageable_type = models.ForeignKey(ContentType)
    imageable_id = models.PositiveIntegerField()
    imageable_object = GenericForeignKey('imageable_type', 'imageable_id')

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GooseDbVersion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version_id = models.BigIntegerField()
    is_applied = models.IntegerField()
    tstamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goose_db_version'


class Images(models.Model):
    uuid = models.CharField(primary_key=True, max_length=36)
    name = models.TextField()
    alt = models.TextField()

    class Meta:
        managed = False
        db_table = 'images'


class Posts(models.Model):
    content = models.TextField()
    title = models.TextField()
    excerpt = models.TextField()

    class Meta:
        managed = False
        db_table = 'posts'

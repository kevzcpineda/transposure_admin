# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcMap(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ac_map'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class PredefinedRoutes(models.Model):
    direction_from = models.TextField()
    direction_to = models.TextField()
    description = models.TextField()
    is_active = models.IntegerField(db_column='is active')  # Field renamed to remove unsuitable characters.
    date_modified = models.DateField()
    date_added = models.DateField()

    def __str__(self):
        return "%s" % (self.direction_from)

    class Meta:
        managed = False
        db_table = 'predefined_routes'


class Profiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    uname = models.CharField(unique=True, max_length=255)
    pword = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_no = models.BigIntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    is_active = models.IntegerField()
    date_created = models.DateField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.fullname)

    class Meta:
        managed = False
        db_table = 'profiles'


class TransitReviews(models.Model):
    commented_by = models.CharField(max_length=255)
    terminal_id = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    star_ratings = models.TextField()
    date_posted = models.DateField()

    class Meta:
        managed = False
        db_table = 'transit_reviews'


class TransitType(models.Model):
    transit_id = models.AutoField(primary_key=True)
    transit_type = models.CharField(max_length=255)
    is_active = models.IntegerField()
    date_created = models.DateField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.transit_type)

    class Meta:
        managed = False
        db_table = 'transit_type'


class Transits(models.Model):
    transit_id = models.IntegerField()
    marker_name = models.TextField()
    slug = models.CharField(max_length=255)
    marker_description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    terminal_rating = models.TextField()
    destination_lat = models.FloatField()
    destination_lang = models.FloatField()
    is_active = models.IntegerField()
    is_show = models.IntegerField()
    is_created = models.DateField(blank=True, null=True)
    date_modified = models.DateField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.slug)


    class Meta:
        managed = False
        db_table = 'transits'


class TransitsBak(models.Model):
    transit_id = models.IntegerField()
    marker_name = models.TextField()
    slug = models.CharField(max_length=255)
    marker_description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    terminal_rating = models.TextField()
    is_active = models.IntegerField()
    is_show = models.IntegerField()
    is_created = models.DateField(blank=True, null=True)
    date_modified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transits_bak'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

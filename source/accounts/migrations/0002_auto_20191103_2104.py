 # Generated by Django 2.2 on 2019-11-03 21:04

from django.db import migrations

def create_profile(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('accounts', 'Profile')
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)

def delete_profiles(apps, schema_editor):
    pass



class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_profile, delete_profiles)
    ]

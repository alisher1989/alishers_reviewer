# Generated by Django 2.2 on 2019-11-16 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20191116_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
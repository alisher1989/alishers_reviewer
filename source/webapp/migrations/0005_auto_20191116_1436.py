# Generated by Django 2.2 on 2019-11-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20191116_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Фото'),
        ),
    ]

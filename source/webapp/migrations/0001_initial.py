# Generated by Django 2.2 on 2019-11-16 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Товар')),
                ('category', models.CharField(choices=[('other', 'Другое'), ('food', 'Еда'), ('clothes', 'Одежда'), ('household', 'Товары для дома')], default='other', max_length=50, verbose_name='Категория')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='описание отзыва')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=None, max_length=50, verbose_name='Рейтинг')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('product', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='webapp.Product')),
            ],
        ),
    ]
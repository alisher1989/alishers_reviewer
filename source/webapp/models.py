from django.conf import settings
from django.db import models

CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('household', 'Товары для дома'),
)



class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар', null=False, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория', null=False, blank=False)
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='описание')
    photo = models.ImageField(upload_to='user_pics', null=True, blank=True, verbose_name='Фото')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


RAITING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                             verbose_name='Author', related_name='reviews')
    product = models.ForeignKey(Product, related_name='product_order', max_length=100, on_delete=models.CASCADE)
    order_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='описание отзыва')
    rating = models.CharField(max_length=50, choices=RAITING_CHOICES, default=None,
                                verbose_name='Рейтинг', null=False, blank=False)

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'





from django.db import models
from django.db.models.fields import SlugField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

class Headphones(Product):

    compatibility = models.CharField(max_length=255, verbose_name='Совместимость')
    working_hours = models.CharField(max_length=255, verbose_name='Время работы')
    radius_of_action = models.CharField(max_length=255, verbose_name='Радиус действия')
    bluetooth_version = models.CharField(max_length=255, verbose_name='Версия bluetooth')
    weight = models.CharField(max_length=255, verbose_name='Вес')
    country = models.CharField(max_length=255, verbose_name='Страна')
    colour = models.CharField(max_length=255, verbose_name='Цвет')
    noise_suppression = models.CharField(max_length=255, verbose_name='Шумоподавление')
    microphone = models.CharField(max_length=255, verbose_name='Микрофон')
    connection_type = models.CharField(max_length=255, verbose_name='Тип подключения')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)
    
    class Meta:
        verbose_name = 'Наушники'
        verbose_name_plural = 'Наушники'

class ProtectiveGlasses(Product):

    compatibility = models.CharField(max_length=255, verbose_name='Совместимость')
    presence_of_a_frame = models.CharField(max_length=255, verbose_name='Наличие рамки')
    form_factor = models.CharField(max_length=255, verbose_name='Форм-Фактор')
    adhesive_layer = models.CharField(max_length=255, verbose_name='Клеевой слой')
    strength = models.CharField(max_length=255, verbose_name='Прочность')
    thickness = models.CharField(max_length=255, verbose_name='Толшина')
    boards = models.CharField(max_length=255, verbose_name='Борты')
    oleophobic_coating = models.CharField(max_length=255, verbose_name='Олеофобное покрытие')
    anti_glare = models.CharField(max_length=255, verbose_name='Антиблик')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)
    
    class Meta:
        verbose_name = 'Защитные стекла'
        verbose_name_plural = 'Защитные стекла'

class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Товар: {} (для корзины)".format(self.product.title)
    
    class Meta:
        verbose_name = 'Товар корзины'
        verbose_name_plural = 'Товары корзины'

class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Корзину'
        verbose_name_plural = 'Корзины'

class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель {} {}".format(self.user.first_name, self.user.last_name)
    
    class Meta:
        verbose_name = 'Покупателя'
        verbose_name_plural = 'Покупатели'

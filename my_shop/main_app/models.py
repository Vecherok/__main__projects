
from distutils.command.sdist import sdist
from django.db import models
#from phone_field import PhoneField
from django.utils.text import slugify



class Clients(models.Model):

    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, unique=True, error_messages='такой email уже зарегистрирован',
                            primary_key=True)
    phone = models.CharField(blank=False, max_length=15)
    adress = models.CharField(max_length=100)
    
    #ordered_product = models.ManyToManyField('Products', related_name="my_products")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self) -> str:
        return self.name


class Category(models.Model):

    category_name = models.CharField('имя категории', max_length=100, db_index=True)
    category_slug = models.SlugField('url категории', max_length=100, unique=True)

    class Meta:
        ordering = ("category_name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.category_name

class Products(models.Model):
    
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    code = models.CharField('Артикул', blank=False, unique=True, error_messages="не уникален, измените", 
                            db_index=True,  max_length=50)
    title = models.CharField('Наименование', blank=False, max_length=100)
    subtitle = models.CharField('Краткое описание', blank=True, max_length=200)
    content = models.TextField('Описание', blank=False, max_length=500)
    product_slug = models.CharField('url товара', max_length=100)  #db_index=True
    image = models.ImageField('Изображение', upload_to='media/uploads', 
                            default="static\main_app\img\image_not_yet_uploaded_by_unitedworldmedia_de1noau-fullview.png")
    price = models.DecimalField('Цена', max_digits=15, decimal_places=2)
    count = models.PositiveIntegerField('Остатки', blank=True, default='0')
    isActive = models.BooleanField('Наличие', default=True)
    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Обновлен',auto_now=True)

    # ordered_by = models.ManyToManyField('Clients', related_name="my_ordes")
    # ordered_by = models.ManyToManyField('Clients', related_name="ordered_by", default="0")

    class Meta:
        ordering = ('title',)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        # index_together = (('id', 'product_slug'),)
        permissions = (('add_produt','add_product'),)

    def __str__(self) -> str:
        return self.title

    # def save(self,  *args, **kwargs):
    #     self.product_slug = slugify(self.title)
    #     return super(Products, self).save(*args, **kwargs)


class Orders(models.Model):

    order_number = models.CharField('Номер заказа', blank=False, unique=True, error_messages="такой номер уже есть", max_length=20)
    order_time = models.DateTimeField()

    ordered_by = models.ForeignKey('Clients', on_delete=models.PROTECT)
    ordered_product = models.ForeignKey('Products', on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    #client = models.ForeignKey("Client", on_delete=models.PROTECT)
    

class Cart(models.Model): pass
    
    
    
    
    
    
    
    # __code = models.CharField('Артикул', blank=False, unique=True, error_messages="не уникален, измените", primary_key=True, max_length=50)
    # __title = models.CharField('Наименование', blank=False, max_length=100)
    # __subtitle = models.CharField('Краткое описание', max_length=200)          #не разрешает оставить пустым???
    # __content = models.TextField('Описание', blank=False, max_length=500)
    # __image = models.ImageField('Изображение', upload_to='media/uploads', default="static\main_app\img\image_not_yet_uploaded_by_unitedworldmedia_de1noau-fullview.png")
    # __product_type = models.CharField('Категория', choices=__PRODUCT_TYPE, max_length=1, blank=False,default="___")
    # __price = models.DecimalField('Цена', max_digits=15, decimal_places=2)
    # __count = models.PositiveIntegerField('Остатки', max_length=2, blank=False, default=0)
    # __isActive = models.CharField('Наличие', choices=__ISACTIVE, max_length=1, blank=False)
    # name = models.CharField(blank=False, max_length=100, unique=True)
    # email = models.EmailField(blank=False, primary_key=True)
    # number = models.CharField(blank=False, max_length=13)
    # adress = models.CharField(max_length=100)
    # client = models.ForeignKey('Author', on_delete=models.CASCADE)      # ?


from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    #国名
    #地域
    #公用語
    #英語レベル
    #通貨
    #首都
    #日本大使館所在地
    #物価レベル
    #国の情報
    #都市情報
    #ツアー情報
    #アイキャッチ画像
    #作成者
    #作成日時
    #投稿日時
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(unique=True, null=True)
    name = models.CharField(max_length=50)
    AREA_CHOICES = (
        ('0','アジア'),
        ('1','オセアニア'),
        ('2','北アメリカ'),
        ('3','中南アメリカ'),
        ('4','ヨーロッパ'),
        ('5','中東'),
        ('6','アフリカ'),
    )
    area = models.CharField(max_length=10, choices=AREA_CHOICES)
    official_language = models.CharField(max_length=50)
    ENGLISH_CHOICES = (
        ('3', '公用語'),
        ('2', '大体通じる'),
        ('1', '観光地のみ通じる'),
        ('0', '通じない'),
    )
    english_level = models.CharField(max_length=10, choices=ENGLISH_CHOICES)
    currency = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    Ja＿embassy = models.CharField(max_length=50)
    PRICE_LEVEL_CHOICES = (
        ('2', '日本より高い'),
        ('1', '日本と同じくらい'),
        ('0', '日本より安い'),
    )
    price_level = models.CharField(max_length=10, choices=PRICE_LEVEL_CHOICES)

    place_info = models.TextField()
    city_info = models.TextField()
    tour_info = models.TextField()
    cover_image = models.ImageField(upload_to='country_images/')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class City(models.Model):
    #都市名
    #国名
    #移動手段情報
    #宿泊先情報
    #名産品情報
    #名所情報
    #その他の情報
    #アイキャッチ画像
    #作成者
    #作成日時
    #投稿日時
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(unique=True, null=True)
    name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
    )
    transfer_info = models.TextField()
    lodge_info = models.TextField()
    specialty_info = models.TextField()
    sights_info = models.TextField()
    other_info = models.TextField()
    cover_image = models.ImageField(upload_to='city_images/')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Image(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Asset(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='assets/')

    def __str__(self):
        return self.title
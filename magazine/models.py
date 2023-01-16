from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default='media/default.jpg', verbose_name="Фото")
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Показывать в главной странице")
    is_main = models.BooleanField(default=True, verbose_name='Show as main news')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})


class Block(models.Model):
    header = models.CharField(max_length=200, null=True, blank=True)
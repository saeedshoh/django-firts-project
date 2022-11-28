from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наимонавание')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создание')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновление')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категории')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
        
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наимонавание')
    
    
    def get_absolute_url(self):
        return reverse("category_id", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
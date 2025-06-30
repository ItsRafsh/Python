from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=200)
    slug_kat = models.SlugField(editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug_kat = slugify(self.nama)
        return super(Kategori, self).save(*args, **kwargs)
    def __str__(self):
        return '{}. {}'.format(self.id, self.nama)

class Youtube(models.Model):
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    rating = models.CharField(max_length=10, choices=RATING_CHOICES)
    Kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    slug_art = models.SlugField(editable=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)        # 👈 Tambahan penting!
    pupdate = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug_art = slugify(self.judul)
        return super(Youtube, self).save(*args, **kwargs)
    def __str__(self):
        return '{}. {}'.format(self.id, self.judul)
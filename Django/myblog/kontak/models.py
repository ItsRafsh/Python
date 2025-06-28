from django.db import models

# Create your models here.

class KontakModel(models.Model):
    nama = models.CharField(max_length=20)
    email = models.EmailField()
    pesan = models.TextField()
    waktu_kirim = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.id, self.nama)


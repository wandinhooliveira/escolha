from django.db import models

# Create your models here.
class Disputa(models.Model):

    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    foto1 = models.ImageField()
    nome1 = models.CharField(max_length=30)
    votos1 = models.PositiveIntegerField(default=0)
    foto2 = models.ImageField()
    nome2 = models.CharField(max_length=30)
    votos2 = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Disputa"
        verbose_name_plural = "Disputas"
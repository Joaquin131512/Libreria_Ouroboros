from django.db import models


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    imagen = models.ImageField(upload_to='services/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services" 

    def __str__(self):
        return self.title
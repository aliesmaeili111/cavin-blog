from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام")
    email = models.EmailField(max_length=100,verbose_name="ایمیل")
    message = models.TextField(blank=True,verbose_name="متن")
    
    class Meta:
        verbose_name="مخاطبین"
        verbose_name_plural="مخاطبین ها"
    
    def __str__(self) :
        return self.email   
    
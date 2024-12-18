from django.db import models


# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    description = models.TextField(max_length=550)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    smtp_server = models.CharField(max_length=255)
    smtp_email = models.CharField(max_length=255)
    smtp_password = models.CharField(max_length=255)
    smtp_port = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    icon = models.ImageField(null=False, upload_to='images/')
    abouts = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.title
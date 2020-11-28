from django.db import models


class ContactUs(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Comment = models.TextField()



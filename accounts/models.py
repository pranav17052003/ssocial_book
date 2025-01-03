from django.contrib.auth.models import AbstractUser, User
from django.db import models
from datetime import date
from django.conf import settings

class CustomUser(AbstractUser):
    public_visibility = models.BooleanField(default=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically calculate age from birth_year
        if self.birth_year:
            self.age = date.today().year - self.birth_year
        super().save(*args, **kwargs)


class UploadedFile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the custom user model
        on_delete=models.CASCADE,
        related_name='uploaded_files'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    visibility = models.BooleanField(default=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    year_published = models.PositiveIntegerField()
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
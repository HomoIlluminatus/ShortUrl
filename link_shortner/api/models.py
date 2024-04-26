from django.db import models
from hashlib import sha256


class ShortLink(models.Model):
    long_url = models.URLField(max_length=2000)
    token = models.CharField(
        max_length=6,
        unique=True,
        blank=True
    )
    click_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-click_count']
        
    def __str__(self):
        return f'{self.long_url} - {self.token}'
from django.db import models
import hashlib
from django.utils import timezone

class ShortLink(models.Model):
    original_url = models.URLField()
    short_url = models.URLField(blank=True)
    hash_value = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.hash_value:
            self.hash_value = self.generate_hash()
        self.short_url = f"http://localhost:8000/short-links/{self.hash_value}"
        super().save(*args, **kwargs)

    def generate_hash(self):
        hasher = hashlib.sha256()
        hasher.update(self.original_url.encode('utf-8'))
        return hasher.hexdigest()[:10]

    def __str__(self):
        return self.short_url

from __future__ import unicode_literals

from django.db import models
from accubits import settings

# Create your models here.


class Library(models.Model):
    book_name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    borrow_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name="borrow")
    author = models.CharField(max_length=100)
    book_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

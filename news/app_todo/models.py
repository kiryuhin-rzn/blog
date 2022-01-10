from django.db import models
from django.contrib.auth.models import User


class TodoListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    date_due = models.DateTimeField(blank=True)

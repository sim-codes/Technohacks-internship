from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=155, blank=True, default='Task')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, blank=False)
    status  = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('todo_detail', args=str(self.id))
    
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=[
        ('work', 'Ish'),
        ('study', 'O\'qish'),
        ('personal', 'Shaxsiy'),
        ('other', 'Boshqa')
    ], default='personal')
    due_date = models.DateField()
    is_important = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-is_important', 'due_date']
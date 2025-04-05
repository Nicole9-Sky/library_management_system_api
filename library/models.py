from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
def get_default_category():
    return Category.objects.first()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=get_default_category)

    def __str__(self):
        return self.title

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='library_user_groups',  # Changed related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='library_user_permissions',  # Changed related_name
        blank=True
    )
    
    def __str__(self):
        return self.username


class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=[('checkout', 'checkout'), ('return', 'return')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action.capitalize()} - {self.book.title} by {self.user.username}"

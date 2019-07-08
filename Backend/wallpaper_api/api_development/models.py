from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    

class api(models.Model):
    name = models.CharField(max_length=120)
    link = models.CharField(max_length=500)
    uploaded_on = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

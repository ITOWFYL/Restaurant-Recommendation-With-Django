from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=100)

class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=7)    # 삭제 시 id 7 -> 기본 항목 참조
    restaurant_name = models.CharField(max_length=100)
    restaurant_link = models.CharField(max_length=500)
    restaurant_content = models.TextField()
    restaurant_keyword = models.CharField(max_length=50)
    

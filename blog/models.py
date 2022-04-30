from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='')
    content=RichTextField()
    isActive=models.BooleanField(default=False)
    isHome=models.BooleanField(default=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

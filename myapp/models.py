from django.db import models

# Create your models here.

class bookcategory(models.Model):
    catname = models.CharField(max_length=50)

    def __str__(self):
        return self.catname


class book(models.Model):
    bookname = models.CharField(max_length=50)
    category = models.ForeignKey(bookcategory,on_delete=models.CASCADE)
    pages = models.IntegerField()
    price = models.IntegerField()
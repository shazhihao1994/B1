from django.db import models
import datetime
class Author(models.Model):
    AuthorID=models.CharField(max_length=200)
    Name=models.CharField(max_length=200)
    Age=models.CharField(max_length=200)
    Country=models.CharField(max_length=200)
    def __unicode__(self):
        return self.AuthorID
class Book(models.Model):
    AuthorID=models.ForeignKey(Author)
    ISBN=models.CharField(max_length=200)
    Title=models.CharField(max_length=200)
    Publisher=models.CharField(max_length=200)
    PublishDate=models.CharField(max_length=200)
    Price=models.CharField(max_length=200) 
    def __unicode__(self):
        return self.Title
        

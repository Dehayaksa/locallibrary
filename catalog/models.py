from django.db import models
from django.urls import reverse
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200,help_text='Enter a book genre (e.g. Sciece Fiction, French Poetry etc.)')
    def __str__(self):
        return self.name

class Meta:
    ordering = ['-my_field_name']
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return self.field_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models
    summary = models.CharField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre=models.ManyToManyField(Genre, help_text="Select a genre for this book")

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_born = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.surname}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    release_date = models.IntegerField()

    def __str__(self):
        return f'{self.title}'



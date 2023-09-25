from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    units = models.IntegerField()

    def __str__(self):
        show = self.name + " por " + self.author
        return show


class User(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)

    def __str__(self):
        show = self.full_name
        return show

class Loan(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        show = self.book_id.name + " prestado por: " + self.user_id.full_name
        return show
    
    
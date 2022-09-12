from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=50)
    book_description = models.CharField(max_length=500)
    book_genre = models.CharField(max_length=50)
    #books_price = models.CharField(max_length=50)
    book_price = models.PositiveSmallIntegerField(default=0)
    book_image = models.ImageField(upload_to='images/', default='')
    book_rate_apple = models.FloatField(default=0)
    book_rate_android = models.FloatField(default=0)
    book_rate_site = models.FloatField(default=0)
    book_show_order = models.PositiveSmallIntegerField(default=0)
    book_free_audio_fragment = models.FileField(upload_to='audio/', default='')
    book_free_pdf_fragment = models.FileField(upload_to='books/pdf/', default='')
    book_free_single_html_fragment = models.FileField(upload_to='books/', default='')
    book_android_link = models.URLField(default='')
    book_favourite_comment = models.ForeignKey('Vote', on_delete=models.SET_NULL, null=True, blank=True, related_name="%(app_label)s_%(class)s_related")

    def __str__(self):
        return self.book_title

    def popular_books(self):
        return str(self.book_genre).strip() == "Популярные"

class Vote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    score = models.IntegerField(default=0)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return str(self.voter) +": " + str(self.score)+" - "+self.comment

class Buyer(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return str(self.buyer) + " " + str(self.book)
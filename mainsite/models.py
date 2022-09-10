from django.db import models


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


    def __str__(self):
        return self.book_title

    def popular_books(self):
        return str(self.book_genre).strip() == "Популярные"

from django.test import TestCase
from django.urls import reverse
import os

from kidsskazki import settings
from .models import Book
# Create your tests here.

#class BookModelTests(TestCase):

#    def test_popular_books(self):
#        """
#        popular() returns False for questions whose filter
#        are wrong.
#        """
#
 #       popular_book = Book()
 #       pass
        #self.assertIs(popular_book.popular_books(), True)


def create_book(title, genre):
    """
    Create a book with the given `title`
    """

    return Book.objects.create(book_title=title,
                                book_genre=genre,
                                book_image=os.path.join(settings.STATIC_ROOT, settings.STATIC_URL, 'mainsite/tst_files/tst_image.jpg'),
                                book_free_single_html_fragment=os.path.join(settings.STATIC_ROOT, settings.STATIC_URL, 'mainsite/tst_files/tst_image.jpg'),
                                book_free_pdf_fragment=os.path.join(settings.STATIC_ROOT, settings.STATIC_URL, 'mainsite/tst_files/tst_image.jpg'),
                                book_free_audio_fragment=os.path.join(settings.STATIC_ROOT, settings.STATIC_URL, 'mainsite/tst_files/tst_image.jpg')
                               )

class BookIndexViewTests(TestCase):
    def test_no_books(self):
        """
        If no books exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No books are available.")
        self.assertQuerysetEqual(response.context['popular_books_list'], [])

    def test_popular_book(self):
        """
        Books with popular genre are displayed on the
        index page.
        """
        book = create_book(title="Test title.", genre = "Popular")
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['popular_books_list'],
            [book],
        )

    def test_sleeping_book(self):
        """
        Books with sleeping genre are displayed on the
        index page.
        """
        book = create_book(title="Test title.", genre = "Sleeping")
        response = self.client.get(reverse('sleeping'))
        self.assertQuerysetEqual(
            response.context['popular_books_list'],
            [book],
        )

    def test_developing_book(self):
        """
        Books with developing genre are displayed on the
        index page.
        """
        book = create_book(title="Test title.", genre = "Developing")
        response = self.client.get(reverse('developing'))
        self.assertQuerysetEqual(
            response.context['popular_books_list'],
            [book],
        )
    def test_two_popular_books(self):
        """
        The index (popular) page may display multiple books.
        """
        book1 = create_book(title="Book title 1.", genre='Popular')
        book2 = create_book(title="Book title 2.", genre='Popular')
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            qs=response.context['popular_books_list'],
            values=[book1, book2],
            ordered=False
        )

    def test_two_sleeping_books(self):
        """
        The sleeping page may display multiple books.
        """
        book1 = create_book(title="Book title 1.", genre='Sleeping')
        book2 = create_book(title="Book title 2.", genre='Sleeping')
        response = self.client.get(reverse('sleeping'))
        self.assertQuerysetEqual(
            qs=response.context['popular_books_list'],
            values=[book1, book2],
            ordered=False
        )

    def test_two_developing_books(self):
        """
        The sleeping page may display multiple books.
        """
        book1 = create_book(title="Book title 1.", genre='Developing')
        book2 = create_book(title="Book title 2.", genre='Developing')
        response = self.client.get(reverse('developing'))
        self.assertQuerysetEqual(
            qs=response.context['popular_books_list'],
            values=[book1, book2],
            ordered=False
        )

class BookDetailViewTests(TestCase):
    def test_book_detail(self):
        """
        The detail view of a book
        displays the book's title.
        """
        book = create_book(title='Test book 1', genre='Popular')
        url = reverse('book_detail', args=(book.id,))
        response = self.client.get(url)
        self.assertContains(response, book.book_title)

    def test_if_book_doesnt_exist(self):
        """
        The detail view of the book that doesn't exist
        returns a 404 not found.
        """
        book = create_book(title='Test book 1', genre='Popular')
        url = reverse('book_detail', args=(book.id+1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
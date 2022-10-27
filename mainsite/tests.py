from django.test import TestCase
from django.urls import reverse
import os

from kidsskazki import settings
from .models import Book, Buyer, Vote
from django.contrib.auth.models import User
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

    def test_popular_title(self):
        """
        Page title Popular (genre) is displayed on the
        index page.
        """
        book = create_book(title="Test title.", genre="Popular")
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['context_title'],
            'Popular',
        )

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

    def test_sleeping_title(self):
        """
        Page title Sleeping (genre) is displayed on the
        Sleeping page.
        """
        book = create_book(title="Test title.", genre="Sleeping")
        response = self.client.get(reverse('sleeping'))
        self.assertQuerysetEqual(
            response.context['context_title'],
            'Sleeping',
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

    def test_developing_title(self):
        """
        Page title Developing (genre) is displayed on the
        Developing page.
        """
        book = create_book(title="Test title.", genre="Developing")
        response = self.client.get(reverse('developing'))
        self.assertQuerysetEqual(
            response.context['context_title'],
            'Developing',
        )
    def test_developing_book(self):
        """
        Books with developing genre are displayed on the
        index page.
        """
        book = create_book(title="Test title.", genre="Developing")
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


def create_buyer(book,user):
    """
    Create a buyer with a given book
    """

    return Buyer.objects.create(book=book,
                                buyer=user,
                                bought=True
                                )
class BuyerDetailViewTests(TestCase):
    def test_buyer_detail(self):
        """
        The list of the books bought (or available) by the user.
        """

        book = create_book(title='Test book 1', genre='Popular')
        user = User.objects.create_user('test_username', 'test_email@crazymail.com', 'mypassword')
        buyer = create_buyer(book=book,
                             user=user)
        #надо добавить авторизацию
        url = reverse('buyer_detail')

        response = self.client.get(url)

        print(response)
        #self.assertQuerysetEqual(
        #    qs=response.context['bought_list'],
        #    values=[buyer],
        #)

        self.assertEqual(response.status_code, 302)
        #self.assertContains(response, "No books are available.")
        #self.assertQuerysetEqual(response.context['popular_books_list'], [])

def create_vote(book, user, comment='Test comment 1'):
    """
    Create a buyer with a given book
    """

    return Vote.objects.create(book=book,
                                voter=user,
                                score=5,
                                comment=comment
                                )

class VoteListViewTests(TestCase):
    def test_vote_list(self):
        """
        Votes on the vote list page.
        """
        book = create_book(title='Test book 1', genre='Popular')
        user = User.objects.create_user('test_username', 'test_email@crazymail.com', 'mypassword')
        vote = create_vote(book=book,
                             user=user)

        response = self.client.get(reverse('vote_list'))
        self.assertQuerysetEqual(
            response.context['vote_list'],
            [vote],
        )

class VoteDetailViewTests(TestCase):
    def test_vote_detail(self):
        """
        The detail view of a vote
        """
        book = create_book(title='Test book 1', genre='Popular')
        user = User.objects.create_user('test_username', 'test_email@crazymail.com', 'mypassword')
        vote = create_vote(book=book, user=user, comment='Test comment 2')
        url = reverse('vote_detail', args=(vote.id,))
        response = self.client.get(url)
        self.assertContains(response, vote.comment)

    def test_if_vote_doesnt_exist(self):
        """
        The detail view of the vote that doesn't exist
        returns a 404 not found.
        """
        book = create_book(title='Test book 1', genre='Popular')
        user = User.objects.create_user('test_username', 'test_email@crazymail.com', 'mypassword')
        vote = create_vote(book=book, user=user, comment='Test comment 2')
        url = reverse('vote_detail', args=(vote.id+1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
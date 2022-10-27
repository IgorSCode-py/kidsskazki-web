from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book, Vote, Buyer


# Create your views here.
class IndexView(generic.ListView):
    """
    Return the top-3 popular books.
    """
    template_name = 'mainsite/popular.html'
    context_object_name = 'popular_books_list'


    def get_queryset(self):
        """
        Return a list of the popular books.
        """

        return Book.objects.filter(
            book_genre="Popular"
        )
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['context_title'] = 'Popular'
        return context

class SleepingView(generic.ListView):
    template_name = 'mainsite/popular.html'
    context_object_name = 'popular_books_list'

    def get_queryset(self):
        """
        Return a list of the sleeping books.
        """
        return Book.objects.filter(
            book_genre="Sleeping"
        )
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['context_title'] = 'Sleeping'
        return context

class DevelopingView(generic.ListView):
    template_name = 'mainsite/popular.html'
    context_object_name = 'popular_books_list'

    def get_queryset(self):
        """
        Return a list of the developing books.
        """
        return Book.objects.filter(
            book_genre = "Developing"
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['context_title'] = 'Developing'
        return context

def book_list(request):
    """
    Return list of popular books (for API).
    """
    books = Book.objects.all()
    data = {"results": list(books.values("book_title", "book_description", "book_genre"))}
    #print(data)
    return JsonResponse(data)

def book_detail_view(request, book_id = 1):
    book = get_object_or_404(Book, pk=book_id)
    vote_list = Vote.objects.filter(book=book)
    context = {
        'book': book,
        'vote_list': vote_list
        }
    return render(request, 'mainsite/book_detail.html', context)

@login_required
def buyer_detail_view(request):
    buyer = request.user
    bought_list = Buyer.objects.filter(buyer=buyer, bought=True)
    #context = super().get_context_data(**kwargs)
    context = {'bought_list': bought_list}

    return render(request, 'mainsite/buyer_detail.html', context)


class VoteDetailView(generic.DetailView):
    model = Vote
    template_name = 'mainsite/vote_detail.html'

class VoteListView(generic.ListView):
    model = Vote
    template_name = 'mainsite/vote_list.html'
    context_object_name = 'vote_list'

class VoteCreate(LoginRequiredMixin, generic.CreateView):
    model = Vote
    fields = '__all__'
    success_url = reverse_lazy('vote_list')


class VoteUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Vote
    fields = '__all__'

class VoteDelete(LoginRequiredMixin, generic.DeleteView):
    model = Vote
    success_url = reverse_lazy('vote_list')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'mainsite/signup.html'
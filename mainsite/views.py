from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic


from .models import Book


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'mainsite/popular.html'#layout
    context_object_name = 'popular_books_list'


    def get_queryset(self):
        """
        Return the top-3 popular books.
        """

        return Book.objects.all()



def book_list(request):
    """
    Return list of popular books (for API).
    """
    books = Book.objects.all()
    data = {"results": list(books.values("book_title", "book_description", "book_genre"))}
    #print(data)
    return JsonResponse(data)


def aboutskazki(request):
    return render(request, "main/aboutskazki.html")

def application(request):
    return render(request, "main/application.html")

def education(request):
    return render(request, "main/education.html")

def relax(request):
    return render(request, "main/relax.html")

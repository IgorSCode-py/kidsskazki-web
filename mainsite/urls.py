
from django.urls import path, include
from . import views
#from .apiviews import BookList
from django.conf.urls.static import static

from kidsskazki import settings

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path("api/", BookList.as_view(), name="books_list"),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

from django.conf.urls.static import static

from kidsskazki import settings

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sleeping', views.SleepingView.as_view(), name='sleeping'),
    path('developing', views.DevelopingView.as_view(), name='developing'),
    path('vote/<int:pk>/', views.VoteDetailView.as_view(), name='vote_detail'),
    path('vote', views.VoteListView.as_view(), name='vote_list'),
    path('book/<int:book_id>/', views.book_detail_view, name='book_detail'),
    path('buyer', views.buyer_detail_view, name='buyer_detail'),#/<int:user_id>/
]
urlpatterns += [
    path('vote/create/$', views.VoteCreate.as_view(), name='vote_create'),
    path('vote/<int:pk>/update/$', views.VoteUpdate.as_view(), name='vote_update'),
    path('vote/<int:pk>/delete/$', views.VoteDelete.as_view(), name='vote_delete'),
    ]
urlpatterns += [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/profile/', views.buyer_detail_view, name='profile'),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

from .views import EbookListCreateApiView

urlpatterns = [
    path('ebooks/', EbookListCreateApiView.as_view(), name='ebook-list'),
]
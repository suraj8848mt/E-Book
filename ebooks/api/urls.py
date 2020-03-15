from django.urls import path

from .views import (EbookListCreateApiView,
                    EbookDetailApiView,
                    ReviewCreateApiView,
                    ReviewDetailApiView)

urlpatterns = [
    path('ebooks/', EbookListCreateApiView.as_view(), name='ebook-list'),
    path('ebooks/<int:pk>/', EbookDetailApiView.as_view(), name='ebook-detail'),
    path('ebooks/<int:ebook_pk>/review',
         ReviewCreateApiView.as_view(),
         name='review-create'),
    path('reviews/<int:pk>/',
         ReviewDetailApiView.as_view(),
         name='review-detail'),
]
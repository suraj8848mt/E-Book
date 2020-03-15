from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer


# class EbookListCreateApiView(mixins.ListModelMixin,
#                              mixins.CreateModelMixin,
#                              generics.GenericAPIView):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class EbookListCreateApiView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class EbookDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class ReviewCreateApiView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)


class ReviewDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



from .serializers import LibrarySerializer
from .models import Library
from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView
from common.custom_exceptions import DevOpsValidationErr
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
import datetime

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.AllowAny,)
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    def list(self, request, *args, **kwargs):
        qs = self.queryset
        data = self.serializer_class(qs, context={'request': request}, many=True).data
        return Response({'result': data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data

        books = Library()
        books.book_name = data['book_name']
        books.book_count = data['book_count']
        books.author = data['author']
        books.created_by = request.user
        books.save()
        return Response({"result": "Books added to Library"}, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=True, url_path='get-book')
    def get_book(self, request, pk):
        """
        Api to get book details
        :param request:
        :param pk: Primary key of Library
        :return:
        """
        query_set = Library.objects.get(id=pk)
        data = self.serializer_class(query_set, context={'request': request}).data
        return Response({'result': data}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='borrow-book')
    def borrow_book(self, request, pk):
        """
        Api to borrow book from Library
        :param request:
        :param pk: Primary key of Library
        :return:
        """
        query_set = Library.objects.get(id=pk)
        query_set.book_count -= 1
        query_set.borrow_by = request.user
        query_set.save()
        return Response({'result': "Book successfully Borrowed"}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='user-borrow-book')
    def user_borrow_book(self, request):
        """
        Api to get book borrowed by user
        :param request:
        :return:
        """
        query_set = Library.objects.get(borrow_by=request.user)
        data = self.serializer_class(query_set, context={'request': request}).data
        return Response({'result': data}, status=status.HTTP_200_OK)


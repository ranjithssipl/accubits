from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Library
from django.contrib.auth.models import Group, Permission
from accubits.defaults import AppDefaults
import datetime
from django.db.models import Q


class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = ('id', 'book_name', 'book_count', 'author', 'created_at', 'created_by')





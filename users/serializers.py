from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import AccubitsUser
from django.contrib.auth.models import Group, Permission
from accubits.defaults import AppDefaults
import datetime
from django.db.models import Q


class UsersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AccubitsUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'name')





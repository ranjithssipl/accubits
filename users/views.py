from users.serializers import UsersSerializer
from users.models import AccubitsUser
from rest_framework import permissions
from rest_framework import viewsets, status
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


def jwt_response_payload_handler(token, user=None, request=None):
    """ Modifying jwt login response details """
    user_details = UsersSerializer(user, context={'request': request}).data

    # """ Fetching assigned accesses for the use """
    # user_details['accesses'] = list()

    return {
        'token': token,
        'user': user_details
    }

"""
User creation, list, view, edit and delete
"""


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.AllowAny,)
    queryset = AccubitsUser.objects.all()
    serializer_class = UsersSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        user = AccubitsUser()
        user.username = data['username']
        user.name = data['name']
        user.email = data['email']
        user.set_password(data['password'])
        user.save()

        return Response({"result": "Users created successfully"}, status=status.HTTP_201_CREATED)




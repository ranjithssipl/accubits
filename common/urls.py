from users.views import UserViewSet
from rest_framework import routers
from .views import BookViewSet
# Defining Router
common_router = routers.DefaultRouter()

common_router.register(r'user', UserViewSet)
common_router.register(r'books', BookViewSet)


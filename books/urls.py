from django.urls import path, include
from .views.auth_views import RegisterView, LoginAPIView, LogoutAPIView
from rest_framework.routers import DefaultRouter
from .views.crud_viewsets import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'author', AuthorViewSet)
router.register(r'book', BookViewSet)


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('search/', BookViewSet.as_view({'get': 'search'})),
    path('', include(router.urls))
]
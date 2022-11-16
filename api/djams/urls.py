from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'genre', GenreViewSet)
router.register(r'song', SongViewSet)
router.register(r'artist', ArtistViewSet)

urlpatterns = [
    # path('song/', SongAPIView.as_view()),
    # path('song/<str:pk>/', SongAPIView.as_view()), #ids
    path('', include(router.urls)),

]
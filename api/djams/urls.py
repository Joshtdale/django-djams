from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'genre', GenreViewSet)
router.register(r'song', SongViewSet)
router.register(r'artist', ArtistViewSet)
router.register(r'album', AlbumViewSet)


urlpatterns = [
    # path('song/', SongAPIView.as_view()),
    # path('song/search/<str:name>/', SongList.as_view()), #ids
    path('song/', SongList.as_view()),
    path('', include(router.urls)),
    # re_path('^purchases/(?P<name>.+)/$', SongList.as_view()),

]
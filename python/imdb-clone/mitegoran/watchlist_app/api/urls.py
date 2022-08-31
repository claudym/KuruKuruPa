from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (MediaListAV,
                                     MediaAV,
                                     StreamPlatformAV,
                                     StreamPlatformListAV)

urlpatterns = [
    path('list/', MediaListAV.as_view(), name='media-list'),
    path('<int:pk>', MediaAV.as_view(), name='media'),
    path('platform/', StreamPlatformListAV.as_view(), name='platform-list'),
    path('platform/<int:pk>', StreamPlatformAV.as_view(), name='platform')
]

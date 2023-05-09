
from django.urls import path, include
from movielist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatfromAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch-detail'),
    path('stream/', StreamPlatfromAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(),
         name='streamplatform-detail'),
]

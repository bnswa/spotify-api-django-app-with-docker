from django.urls import path
from . import views

urlpatterns = [
    path('top-tracks/', views.get_top_tracks, name='get_top_tracks'),
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),
    # URL pattern for the create_playlist_form view
    path("create-playlist/", views.create_playlist_view, name="create-playlist-form"),
    # URL pattern for the create_playlist_view
    path("create-playlist-view/", views.create_playlist_view, name="create-playlist-view")
  
]

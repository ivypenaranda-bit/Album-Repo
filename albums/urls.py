from django.urls import path
from . import views

app_name = 'albums'

urlpatterns = [
    path('', views.AlbumListView.as_view(), name='album-list'),
    path('albums/create/', views.AlbumCreateView.as_view(), name='album-create'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album-detail'),
    path('albums/<int:pk>/update/', views.AlbumUpdateView.as_view(), name='album-update'),
    path('albums/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album-delete'),
    path('albums/<int:album_pk>/photos/add/', views.PhotoCreateView.as_view(), name='photo-add'),
    path('photos/<int:pk>/update/', views.PhotoUpdateView.as_view(), name='photo-update'),
    path('photos/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo-delete'),
]

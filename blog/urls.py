from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name = 'starting-page'),
    path('posts', views.AllPostsView.as_view(), name = 'posts-page'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name = 'post-detail-page'),
    path('read-later', views.ReadLaterView.as_view(), name='read-later'),
    path('remove-read-later', views.RemoveReadLaterView.as_view(), name='remove-read-later'),
] 
   
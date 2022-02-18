from django.urls import path
from blogs.views import PostList, PostDetails, PostCreateView, PostUpdateView, PostDeleteView
from blogs.feeds import LatestPostsFeed


app_name = 'blogs'

urlpatterns = [
    path('', PostList.as_view(), name='all'),
    path('create/', PostCreateView.as_view(), name='create'),  # this must be before 'details'
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', PostDetails.as_view(), name='post_detail'),
    path('feed/rss/', LatestPostsFeed(), name='post_feed'),


]

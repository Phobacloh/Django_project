from django.urls import path
from . import views
# from django.views.generic.detail import User
app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('user-profile/', views.StoryViewByAuthor.as_view(), name='UserProfile'),
   
    path('author-list/', views.AuthorListView.as_view(), name='authorList'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='authorDetail'),
    path('update-details/<int:pk>/', views.StoryUpdateView.as_view(), name='storyUpdate'),
]

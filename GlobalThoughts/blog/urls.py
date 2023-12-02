from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

urlpatterns = [
    path('', views.base, name="HomePage"),
   path('home/', PostListView.as_view(), name="Home"),
   path('home/user/<str:username>', UserPostListView.as_view(), name="user-posts"),
   path('post/<int:pk>', PostDetailView.as_view(), name="Post-detail"),
   path('post/new/', PostCreateView.as_view(), name="Post-create"),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name="Post-update"),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="Post-delete"),
   path('about/', views.about, name="About"),
   
]
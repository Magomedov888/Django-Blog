from django.urls import path
from .views import HomePage, PostCreateView, PostDetailView, PostEditView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('posts/new/', PostCreateView.as_view(), name='new_post'),
    path('posts/<int:pk>/edit/', PostEditView.as_view(), name='post_edit')
]
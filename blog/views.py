from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Post

class HomePage(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'

class PostEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

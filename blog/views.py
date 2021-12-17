from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.views.generic.edit import CreateView
class PostListView(ListView):
    pass

class PostDetailsView(DetailView):
    pass

class PostDeleteView(DeleteView):
    pass
class PostCreateView(CreateView):
    pass

from django.urls import path
from django.views.generic import TemplateView
from .views import PostListView, PostDetailsView
app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/post_list.html") , name='listposts'),
    path('<int:pk>/', TemplateView.as_view(template_name="blog/post_details.html"), name='postdetails'),
    path('create-post/', TemplateView.as_view(template_name="blog/post_create.html"), name='postcreate'),
]

from django.urls import path
from .views import PostList,PostDetail

app_name = "blog_api"

urlpatterns = [
    path('', PostList.as_view() , name='listcreate_api'),
    path('<int:pk>/', PostDetail.as_view(), name='postdetails_api'),
    #path('create-post/', TemplateView.as_view(template_name="blog/post_create.html"), name='postcreate_api'),
]

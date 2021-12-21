from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blogapp')),
    path('api/', include('blog_api.urls', namespace='blogapp_api')),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, blog_post_list, create_blog_post, edit_blog_post, delete_blog_post, register_view

router = DefaultRouter()
router.register('api/posts', BlogPostViewSet, basename='blogpost')

urlpatterns = [
    path('register/', register_view, name='register'),
    path('', blog_post_list, name='blog-posts'),
    path('create/', create_blog_post, name='create-post'),
    path('edit/<int:pk>/', edit_blog_post, name='edit-post'),
    path('delete/<int:pk>/', delete_blog_post, name='delete-post'),
    path('', include(router.urls)),
]



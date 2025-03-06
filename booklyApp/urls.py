from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booklyApp import views

router = DefaultRouter()
# to admin
router.register(r'gender', views.GenderViewSet, basename = 'gender')
router.register(r'books', views.BookViewSet, basename = 'books')
router.register(r'authors', views.AuthorViewSet, basename = 'authors')

# to users
router.register(r'reviews', views.ReviewViewSet, basename = 'reviews')
router.register(r'likes', views.LikeViewSet, basename = 'likes')
router.register(r'favorites', views.FavoriteViewSet, basename = 'favorites')
router.register(r'comments', views.CommentViewSet, basename = 'comments')

# to users and not auth (when creating user)
router.register(r'users', views.UserViewSet, basename = 'users')

urlpatterns = [
    path('', include(router.urls)),
    path('reviews-feed/', views.ReviewFeed.as_view(), name = 'reviews-feed')
]
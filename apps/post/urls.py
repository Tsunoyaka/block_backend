from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LikePostView, PostViewSet, CommentCreateDeleteView, TagViewSet


router = DefaultRouter()
router.register('post', PostViewSet, 'post')
router.register('comment', CommentCreateDeleteView)
router.register('tags', TagViewSet, 'tags')

urlpatterns = [
    path('liked/', LikePostView.as_view(), name='liked')
]

urlpatterns += router.urls
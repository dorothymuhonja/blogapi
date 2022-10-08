# from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CommentViewSet
#from .views import PostList, PostDetail, UserList, UserDetail

router = SimpleRouter()
# router.register('users', UserViewSet, basename='users')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = router.urls
from api.views import CommentViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r"posts/(?P<post_id>\d+)/comments",
                CommentViewSet,
                basename="comments")
router.register(r"groups", GroupViewSet)
router.register(r"posts", PostViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/api-token-auth/",
         views.obtain_auth_token,
         name='api-token-auth'),
]

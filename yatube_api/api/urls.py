from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r"posts/(?P<post_id>\d+)/comments",
                   CommentViewSet,
                   basename="comments")
v1_router.register(r"groups", GroupViewSet)
v1_router.register(r"posts", PostViewSet)

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/api-token-auth/",
         views.obtain_auth_token,
         name='api-token-auth'),
]

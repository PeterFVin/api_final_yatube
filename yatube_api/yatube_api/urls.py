from api.views import FollowViewSet, GroupViewSet, PostViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='posts')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'comments', FollowViewSet, basename='comments')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path("api/", include("api.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

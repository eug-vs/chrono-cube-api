from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from timer.views import SolutionViewSet
from users.views import UserViewSet


router = DefaultRouter()
router.register('solutions', SolutionViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

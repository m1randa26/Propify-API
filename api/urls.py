from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

router.register(r'users', UserViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'rental-history', RentalHistoryViewSet)

urlpatterns = [
    path('propify/', include(router.urls))
]
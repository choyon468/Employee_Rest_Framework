from django.urls import path, include
from .views import home
from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

# rest operation for get, put, etc
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('srvc/', include(router.urls)),
]

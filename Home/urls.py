from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet
from .views import InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoice-details', InvoiceDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


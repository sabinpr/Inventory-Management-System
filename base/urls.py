from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductTypeViewSet, DepartmentViewSet, VendorViewSet, PurchaseViewSet, SellViewSet

router = DefaultRouter()
router.register('product-types', ProductTypeViewSet)
router.register('departments', DepartmentViewSet)
router.register('vendors', VendorViewSet)
router.register('products', ProductViewSet)
router.register('purchases', PurchaseViewSet)
router.register('sells', SellViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

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
    path('product/',
         ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product/<int:pk>/',
         ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('department/',
         DepartmentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('department/<int:pk>/',
         DepartmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('product-type/',
         ProductTypeViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product-type/<int:pk>/',
         ProductTypeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('purchase/',
         PurchaseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('purchase/<int:pk>/',
         PurchaseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('sell/',
         SellViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('sell/<int:pk>/',
         SellViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('vendor/',
         VendorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('vendor/<int:pk>/',
         VendorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))
]

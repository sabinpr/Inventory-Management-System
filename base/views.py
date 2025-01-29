from rest_framework import viewsets, permissions, status
from .models import Product, ProductType, Department, Vendor, Purchase, Sell
from .serializers import ProductSerializer, ProductTypeSerializer, DepartmentSerializer, VendorSerializer, PurchaseSerializer, SellSerializer
from rest_framework.response import Response
# Create your views here.88


# class ProductTypeViewSet(viewsets.ModelViewSet):
#     queryset = ProductType.objects.all()
#     serializer_class = ProductTypeSerializer
#     # permission_classes = [permissions.IsAuthenticated]
class ProductTypeViewSet(viewsets.GenericViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def list(self, request):
        product_type_objs = self.get_queryset()
        serializer = self.get_serializer(product_type_objs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        product_type_obj = self.get_object()
        serializer = self.get_serializer(product_type_obj)
        return Response(serializer.data)

    def update(self, request, pk):
        product_type_obj = self.get_object()
        serializer = self.get_serializer(product_type_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        product_type_obj = self.get_object()
        serializer = self.get_serializer(
            product_type_obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        product_type_obj = self.get_object()
        product_type_obj.delete()
        return Response()


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    # permission_classes = [permissions.IsAuthenticated]

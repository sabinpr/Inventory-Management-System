from rest_framework import viewsets, permissions, status
from .models import Product, ProductType, Department, Vendor, Purchase, Sell, User
from .serializers import ProductSerializer, ProductTypeSerializer, DepartmentSerializer, VendorSerializer, PurchaseSerializer, SellSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
# Create your views here.88


# class ProductTypeViewSet(viewsets.ModelViewSet):
#     queryset = ProductType.objects.all()
#     serializer_class = ProductTypeSerializer
#     # permission_classes = [permissions.IsAuthenticated]
class ProductTypeViewSet(viewsets.GenericViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]

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


class DepartmentViewSet(viewsets.GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]

    def list(self, request):
        department_objs = self.get_queryset()
        serializer = self.get_serializer(department_objs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        department_objs = self.get_object()
        serializer = self.get_serializer(department_objs)
        return Response(serializer.data)

    def update(self, request, pk):
        department_objs = self.get_object()
        serializer = self.get_serializer(department_objs, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        department_objs = self.get_object()
        serializer = self.get_serializer(
            department_objs, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        department_objs = self.get_object()
        department_objs.delete()
        return Response()


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]

    def list(self, request):
        purchase_objs = self.get_queryset()
        serializer = self.get_serializer(purchase_objs, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = request.data.get('user')
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        purchase_obj = self.get_object()
        serializer = self.get_serializer(purchase_obj)
        return Response(serializer.data)

    def update(self, request, pk):
        purchase_obj = self.get_object()
        serializer = self.get_serializer(purchase_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        purchase_obj = self.get_object()
        serializer = self.get_serializer(
            purchase_obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        purchase_obj = self.get_object()
        purchase_obj.delete()
        return Response()


class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]


@api_view(['POST'])
@permission_classes([])
def register_api_view(request):
    password = request.data.get('password')
    hash_password = make_password(password)
    data = request.data.copy()
    data['password'] = hash_password
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([])
def login_api_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)

    if user == None:
        return Response({'detail': 'Invalid Credentials!'}, status=status.HTTP_400_BAD_REQUEST)

    token, _ = Token.objects.get_or_create(user=user)

    return Response(token.key)

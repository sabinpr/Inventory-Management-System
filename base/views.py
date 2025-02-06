from rest_framework import viewsets, permissions, status
from .models import Product, ProductType, Department, Vendor, Purchase, Sell, User
from .serializers import ProductSerializer, ProductTypeSerializer, DepartmentSerializer, VendorSerializer, PurchaseSerializer, SellSerializer, UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.core.mail import send_mail
# Create your views here.88


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


class DepartmentViewSet(viewsets.GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

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


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def create(self, request):
        data = request.data.copy()
        data["user"] = request.user.id
        serializer = self.get_serializer(data=data)

        context = {}
        if serializer.is_valid():
            serializer.save()
            try:
                send_mail(
                    subject=f'Purchase Confirmation:',
                    message=f'''Succesfully Purchased by {
                        request.user.email}.''',
                    from_email=None,
                    recipient_list=['sabinprajapati7@gmail.com'],
                    fail_silently=False
                )
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    # permission_classes = [permissions.IsAuthenticated,
    #   permissions.DjangoModelPermissions]


@ api_view(['POST'])
@ permission_classes([permissions.IsAuthenticated])
def register_api_view(request):
    if request.user.groups.name == 'Management':
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

    else:
        return Response({'detail': 'You do not have permissions'}, status=status.HTTP_403_FORBIDDEN)


@ api_view(['POST'])
@ permission_classes([])
def login_api_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)

    if user == None:
        return Response({'detail': 'Invalid Credentials!'}, status=status.HTTP_400_BAD_REQUEST)

    token, _ = Token.objects.get_or_create(user=user)

    return Response(token.key)


@ api_view(['GET'])
@ permission_classes([])
def group_api_view(request):
    group_objs = Group.objects.all()
    serializer = GroupSerializer(group_objs, many=True)

    return Response(serializer.data)

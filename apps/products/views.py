from django.core.mail import send_mail
from django.conf import settings
from apps.products.models import Brand, Color, ModelP, Product, Size
from apps.products.serializers import BrandSerializer, ColorSerializer, ModelPSerializer, ProductSerializer, SizeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import Staff
# Create your views here.

class view_brand(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request):
        staff = request.GET["staff"]
        user = Staff.objects.get(id=staff)
        request.data["created_by"] = user.names

        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        staff = request.GET["staff"]
        brand =  request.GET["brand"]
        user = Staff.objects.get(id=staff)
        brand = Brand.objects.get(id = brand)
        request.data["created_by"] = user.names

        serializer = SizeSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        brand= request.GET["brand"]
        staff = request.GET["staff"]
        brand= ModelP.objects.get(id=brand)
        staff =  Staff.objects.get(id=staff)
        # product.delete()
        if staff.role.name in ["administrador", "supervisor"]:
            brand.deleted  = not brand.deleted
            brand.save(update_fields=['deleted'])

            return Response({"message": "Marca eliminada exitosamente."}, status=status.HTTP_202_OK)

        else:
            return Response({"message": "Usted no tiene permisos de administrador."}, status=status.HTTP_401_UNAUTHORIZED)

class view_color(APIView):
    def get(self, request):
        color = Color.objects.all()
        serializer = ColorSerializer(color, many=True)
        return Response(serializer.data)

    def post(self, request):
        staff = request.GET["staff"]
        user = Staff.objects.get(id=staff)
        request.data["created_by"] = user.names
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        staff = request.GET["staff"]
        color =  request.GET["color"]
        user = Staff.objects.get(id=staff)
        color = Color.objects.get(id = color)
        request.data["created_by"] = user.names

        serializer = SizeSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        color= request.GET["color"]
        staff = request.GET["staff"]
        color= ModelP.objects.get(id=color)
        staff =  Staff.objects.get(id=staff)
        # product.delete()
        if staff.role.name in ["administrador", "supervisor"]:
            color.deleted  = not color.deleted
            color.save(update_fields=['deleted'])

            return Response({"message": "Color eliminado exitosamente."}, status=status.HTTP_202_OK)
        
        else:
            return Response({"message": "Usted no tiene permisos de administrador."}, status=status.HTTP_401_UNAUTHORIZED)

class view_modelp(APIView):
    def get(self, request):
        modelp = ModelP.objects.all()
        serializer = ModelPSerializer(modelp, many=True)
        return Response(serializer.data)

    def post(self, request):
        staff = request.GET["staff"]
        user = Staff.objects.get(id=staff)
        request.data["created_by"] = user.names
        serializer = ModelPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        staff = request.GET["staff"]
        modelp =  request.GET["modelp"]
        user = Staff.objects.get(id=staff)
        modelp = ModelP.objects.get(id = modelp)
        request.data["created_by"] = user.names

        serializer = ModelPSerializer(modelp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        modelp= request.GET["model"]
        staff = request.GET["staff"]
        modelp= ModelP.objects.get(id=modelp)
        staff =  Staff.objects.get(id=staff)
        # product.delete()
        if staff.role.name in ["administrador", "supervisor"]:
            modelp.deleted  = not modelp.deleted
            modelp.save(update_fields=['deleted'])

            return Response({"message": "Talla eliminada exitosamente."}, status=status.HTTP_202_OK)
        
        else:
            return Response({"message": "Usted no tiene permisos de administrador."}, status=status.HTTP_401_UNAUTHORIZED)

class view_size(APIView):
    def get(self, request):
        size = Size.objects.all()
        serializer = SizeSerializer(size, many=True)
        return Response(serializer.data)

    def post(self, request):
        staff = request.GET["staff"]
        user = Staff.objects.get(id=staff)
        request.data["created_by"] = user.names
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        staff = request.GET["staff"]
        size =  request.GET["size"]
        user = Staff.objects.get(id=staff)
        size = Size.objects.get(id = size)
        request.data["created_by"] = user.names

        serializer = SizeSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        size= request.GET["size"]
        staff = request.GET["staff"]
        size= Size.objects.get(id=size)
        staff =  Staff.objects.get(id=staff)
        # product.delete()
        if staff.role.name in ["administrador", "supervisor"]:
            size.deleted  = not size.deleted
            size.save(update_fields=['deleted'])

            return Response({"message": "Talla eliminada exitosamente."}, status=status.HTTP_202_OK)
        
        else:
            return Response({"message": "Usted no tiene permisos de administrador."}, status=status.HTTP_401_UNAUTHORIZED)

class view_product(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        staff = request.GET["staff"]
        user = Staff.objects.get(id=staff)
        request.data["created_by"] = user.names
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        staff= request.GET["staff"]
        price_new = request.data["price"]
        product= request.GET["product"]
        user = Staff.objects.get(id = staff)
        request.data["created_by"] = user.names
        users = Staff.objects.filter(Q(id=staff) | Q(role__name__in=["administrador", "supervisor"]))
        product = Product.objects.get(id = product)
        print(product.price)

        if product.price != price_new:
            for  user in users:
                subject = f'Cambio en precio de producto {product.name} con ID: {product.id}'
                message = f'Cambio en precio de producto {product.name} con ID: {product.id} su nuevo precio es {price_new}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email,]
                send_mail( subject, message, email_from, recipient_list )
        else:
            None

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        product= request.GET["product"]
        staff = request.GET["staff"]
        product= Product.objects.get(id=product)
        staff =  Staff.objects.get(id=staff)
        # product.delete()
        if staff.role.name in ["administrador", "supervisor"]:
            product.deleted  = not product.deleted

            product.save(update_fields=['deleted'])

            return Response({"message": "Producto eliminado exitosamente."}, status=status.HTTP_202_OK)
        
        else:
            return Response({"message": "Usted no tiene permisos de administrador."}, status=status.HTTP_401_UNAUTHORIZED)


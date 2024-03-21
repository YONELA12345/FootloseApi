from urllib import request
from django.core.mail import send_mail
from django.conf import settings
from apps.products.models import Brand, Color, ModelP, Product, Size
from apps.products.serializers import BrandSerializer, ColorSerializer, ImageSerializer, ModelPSerializer, ProductSerializer, SizeSerializer, onget_product_serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.conf import settings
import os

from apps.users.models import Staff, StaffRole
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
        f = Q()
        if 'color' in request.GET:
            f &= Q(id = request.GET['color'])
        return Response(
            ColorSerializer(
                Color.objects.filter(f).order_by('-id'),
                many = True
            ).data
        )

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
        f = Q()
        if 'modelp' in request.GET:
            f &= Q(id = request.GET['modelp'])
        return Response(
            ModelPSerializer(
                ModelP.objects.filter(f).order_by('-id'),
                many = True
            ).data
        )
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
        f = Q()
        if 'size' in request.GET:
            f &= Q(id = request.GET['size'])
        return Response(
            SizeSerializer(
                Size.objects.filter(f).order_by('-id'),
                many = True
            ).data
        )

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
        f = Q()
        if 'product' in request.GET:
            f &= Q(id = request.GET['product'])
        return Response(
            onget_product_serializer(
                Product.objects.filter(f).order_by('-id'),
                many = True
            ).data
        )

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
            product = request.GET.get("product")
            staff = request.GET.get("staff")

            try:
                product = Product.objects.get(id=product)
                staff = Staff.objects.get(id=staff)
            except (Product.DoesNotExist, Staff.DoesNotExist):
                return Response({"message": "Producto o personal no encontrado."}, status=status.HTTP_404_NOT_FOUND)

            if staff.role.name in ["administrador", "supervisor"]:
                product.deleted = not product.deleted
                product.save()
                return Response({"message": "Producto eliminado exitosamente."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Usted no tiene permisos de administrador."}, status=status.HTTP_401_UNAUTHORIZED)

class view_image(APIView):

    def get(self, request):
        product_id = request.GET.get("product")
        if product_id:
            try:
                product = Product.objects.get(id=product_id)
                serializer = ImageSerializer(product)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Se requiere el parámetro 'product' en la solicitud"}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request):
        product= request.GET["product"]
        product = Product.objects.get(id = product)

        serializer = ImageSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class view_filter_products(APIView):
    
    def get(self, request):

        f = Q(deleted=False)
        if 'brand' in request.GET:
            f &= Q(brand=request.GET['brand'])
        if 'modelp' in request.GET:
            f &= Q(modelp=request.GET['business'])
        if 'color' in request.GET:
            f &= Q(color=request.GET['color'])
        if 'size' in request.GET:
            f &= Q(size=  request.GET['size'])
        if 'search' in request.GET:
            print(request.GET['search'])
            f &= Q(name__icontains=request.GET['search'])



        return Response(
            onget_product_serializer(
                Product.objects.filter(f).order_by('-id'),
                many = True
            ).data
        )

def show_image(request, image_path):
    # Construye la ruta completa del archivo de imagen
    full_path = os.path.join(settings.MEDIA_ROOT, image_path)

    try:
        # Abre el archivo de imagen y lo lee en la respuesta HTTP
        with open(full_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/png')
    except FileNotFoundError:
        return HttpResponse(status=404)
    

def get_product_image(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        image_path = product.image.path  # Ruta completa de la imagen

        with open(image_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/png')

    except Product.DoesNotExist:
        return HttpResponseNotFound("La imagen del producto no se encontró")

    except FileNotFoundError:
        return HttpResponseNotFound("La imagen del producto no se encontró")


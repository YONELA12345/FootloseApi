from django.shortcuts import render

from apps.products.models import Brand, Color, ModelP, Product, Size
from apps.products.serializers import BrandSerializer, ColorSerializer, ModelPSerializer, ProductSerializer, SizeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class view_brand(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        brand = Brand.objects.get(pk=pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        brand = Brand.objects.get(pk=pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class view_color(APIView):
    def get(self, request):
        color = Color.objects.all()
        serializer = ColorSerializer(color, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        color = Color.objects.get(pk=pk)
        serializer = ColorSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        color = Color.objects.get(pk=pk)
        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class view_modelp(APIView):
    def get(self, request):
        modelp = ModelP.objects.all()
        serializer = ModelPSerializer(modelp, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ModelPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        modelp = ModelP.objects.get(pk=pk)
        serializer = ModelPSerializer(modelp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        modelp= ModelP.objects.get(pk=pk)
        modelp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class view_size(APIView):
    def get(self, request):
        size = Size.objects.all()
        serializer = SizeSerializer(size, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        size = Size.objects.get(pk=pk)
        serializer = SizeSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        modelp= Size.objects.get(pk=pk)
        modelp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class view_product(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        size = Product.objects.get(pk=pk)
        serializer = ProductSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        modelp= Product.objects.get(pk=pk)
        modelp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
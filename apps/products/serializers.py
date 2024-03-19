from rest_framework import serializers
from .models import Brand, Product, Color, ModelP,  Size

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

    def create(self, validated_data):
        brand=Brand(**validated_data)
        brand.save()
        print("Se guardo")
        return brand

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save(update_fields=validated_data.keys())
        return instance

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"
    
    def create(self, validated_data):
        color=Color(**validated_data)
        color.save()
        print("Se aguardo")
        return color

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save(update_fields=validated_data.keys())
        return instance


class ModelPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelP
        fields = "__all__"
    
    def create(self, validated_data):
        modelp=ModelP(**validated_data)
        modelp.save()
        print("Se aguardo")
        return modelp

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save(update_fields=validated_data.keys())
        return instance

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"
    
    def create(self, validated_data):
        size=Size(**validated_data)
        size.save()
        print("Se aguardo")
        return size

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save(update_fields=validated_data.keys())
        return instance

class ProductSerializer(serializers.ModelSerializer):
    # marca = BrandSerializer()
    # color = ColorSerializer()
    # modelo = ModelPSerializer()
    # tallas = SizeSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
    
    def create(self, validated_data):
        product=Product(**validated_data)
        product.save()
        print("Se aguardo")
        return product

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save(update_fields=validated_data.keys())
        return instance
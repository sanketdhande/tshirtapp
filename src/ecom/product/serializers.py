from rest_framework import serializers

from .models import Product

class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')



class ProductList(serializers.ListSerializer):
    child = ProductListSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')

    def create(self, validated_data):
        print(validated_data, "-----------------------")
        books = [Product(**item) for item in validated_data]
        return self.child.objects.bulk_create(books)

class ProductSerializer(serializers.Serializer):
    product = ProductList(many=True)
    # class Meta:
    #     list_serializer_class = ProductList
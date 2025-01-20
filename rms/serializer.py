from rest_framework import serializers
from .models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class Categoryserializers(serializers.ModelSerializer):
    class Meta():
        model = Category
        #to access fielDS we can acces by using any 3 different types:
        
        #type1:#kun kun custom fields haru serialize garne 
        # fields=[ 'category_name'] 
        
        #type2:
        fields= '__all__' # this is an option if you want to access a available fields in DB


        #type3: using exclude (exclude le mention gareko fields lai matra dhekahudaina)
        # exclude = ['id']
        
    def save(self, **kwargs):
        validated_data = self.validated_data
        number=self.Meta.model.objects.filter(category_name = validated_data.get('category_name')).count()
        if number > 0:
            raise serializers.ValidationError(
                "Category already exists"
            )
        category = self.Meta.model(**validated_data)
        category.save() 
        return category
    
  

      
# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     category_name = serializers.CharField() # from models.py functin Category which has attribute category_name
#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.category_name = validated_data.get("category_name", instance.category_name)
#         instance.save()
#         return instance
        
class FoodSerializer(serializers.ModelSerializer): 
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source = 'category'
    )
    category = serializers.StringRelatedField()
    price_tax = serializers.SerializerMethodField()

    class Meta():
        model=Food
        fields = [
            'id',
            'food_name',
            'food_price',
            'category_id',
            'category',
            'price_tax'
            ]
    def get_price_tax(self, obj:Food):
        return obj.food_price * 0.13 + obj.food_price


class OrderItemSerializer(serializers.ModelSerializer):
    food_id = serializers.PrimaryKeyRelatedField(
        queryset = Food.objects.all(),
        source = 'food' 
        #The source parameter indicates the attribute on the OrderItem model that this field corresponds to. In this case, it suggests that ...
        #the OrderItem model has a foreign key relationship to the Food model, and the field in the OrderItem model that holds this relationship is named food.
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'food_id']  
        

class OrderSerializer(serializers.ModelSerializer):
    
    user = serializers.HiddenField(default = serializers.CurrentUserDefault()) 
    #user field lai hide gara but they can still BE USED TO STORE DATA and jo user logged in xa currently, tesko id leu 
    
    #the Meta class is a way to give your serializer clear instructions on how to handle data. 
    #The Meta class tells the serializer which database model it should work with.
    items = OrderItemSerializer(many = True) # This is a nested serializer for related items
   
    class Meta:
        model = Order
        fields = [
            'user',  # Thiese fields should match a field in the Order model
            'table',
            'total_price',
            'order_status',
            'payment_status',
            'items' # This is a nested serializer field
            
            ]

        
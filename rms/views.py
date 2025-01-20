from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from .serializer import *
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filter
from .filters import *
# from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework import status



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    serializer_class = Categoryserializers
    permission_classes = [IsAuthenticatedOrReadOnly]   
    # filter_backends = [filters.SearchFilter]  
    search_fields = ['category_name' ]
    
    def destroy(self, request, *args, **kwargs):
       
        category_get_pk = self.get_object()
        order_item = OrderItem.objects.filter(food__category=category_get_pk).count()
        if order_item > 0:
            return Response({
                "detail":"Order item exist in category! cant delete"
            })
        category_get_pk.delete()
        return Response({
            "detail":"Category deleted"
        },status= status.HTTP_404_NOT_FOUND)
   
        
# class Categorylist(ListAPIView, CreateAPIView): #the Category class will inherit listAPIview
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
    # def get(self, request):
    #     category = Category.objects.all() #from models.py
    #     serializer = CategorySerializer(category, many=True)
    #     return Response(serializer.data)
    # def post(self, request): #request.method =="POST"
    #     serializer=CategorySerializer(data= request.data)
    #     serializer.is_valid(raise_exception=True) #is_valid checks if the data send by user is valid or not
    #     serializer.save()
    #     return Response({
    #         "detail": "Category added"
    #     })


# @api_view(['GET','POST']) #decorater

# def category_list(request):
#     if request.method =="GET":
#         category = Category.objects.all() #from models.py
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)
#     else: #request.method =="POST"
#         serializer=CategorySerializer(data= request.data)
#         serializer.is_valid(raise_exception=True) #is_valid checks if the data send by user is valid or not
#         serializer.save()
#         return Response({
#             "detail": "Category added" 
#         })
    
    
# class CategoryDetailViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     def destroy(self, request, *args, **kwargs):
       
#         category_get_pk = self.get_object()
#         order_item = OrderItem.objects.filter(food__category=category_get_pk).count()
#         if order_item > 0:
#             return Response({
#                 "detail":"Order item exist in category! cant delete"
#             })
#         category_get_pk.delete()
#         return Response({
#             "detail":"Category deleted"
#         })
        
# class CategoryDetail(RetrieveAPIView, DestroyAPIView,UpdateAPIView):
    
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    # def get(self, request, pk):
    #     category_get_pk = Category.objects.get(pk = pk) 
    #     serializer = CategorySerializer(category_get_pk) #each id of category is serialized
    #     return Response(serializer.data) 
    
    # def delete(self, request, pk):
    #     category_get_pk = Category.objects.get(pk = pk)
    #     order_item = OrderItem.objects.filter(food__category=category_get_pk).count()
    #     if order_item > 0:
    #         return Response({
    #             "detail":"Order item exist in category! cant delete"
    #         })
    #     category_get_pk.delete()
    #     return Response({
    #         "detail":"Category deleted"
    #     })
    # def put(self, request, pk):
    #     category_get_pk = Category.objects.get(pk = pk)
    #     serializer=CategorySerializer(category_get_pk, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({
    #         "detail":"Category has been updated"
    #     })
        
        
     
        
# @api_view(['GET', 'DELETE', 'PUT'])
# def category_detail(request,pk):
#     category_get_pk = Category.objects.get(pk = pk) 
#     if request.method=="GET":
#         serializer = CategorySerializer(category_get_pk)
#         return Response(serializer.data)
#     elif request.method=="DELETE":
#         order_item=OrderItem.objects.filter(food__category=category_get_pk).count()
#         if order_item > 0:
#             return Response({
#                 "detail":"Order item exist in category! cant delete"
#             })
#         category_get_pk.delete()
#         return Response({
#             "detail":"Category deleted"
#         })
#     elif request.method=="PUT":
#         serializer=CategorySerializer(category_get_pk, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "detail":"Category has been updated"
#         })
    
    



class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  
    filter_backends = (filters.DjangoFilterBackend, ) 
    # filterset_fieds = ('category')
    filterset_class = FoodFilter
    search_fields = ['food_name']
    pagination_class = PageNumberPagination
     
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('items').all() #the prefetch_
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset= OrderItem.objects.all()
    serializer_class = OrderItemSerializer
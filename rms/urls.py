from django.urls import path, include
from .views import *
from rest_framework import routers

#create router 
router = routers.SimpleRouter()
router.register(r'category_list', CategoryViewSet, basename='category')
router.register(r'food_list', FoodViewSet, basename='foods')
router.register(r'order_list',OrderViewSet, basename='order')
router.register(r'order_item_list', OrderItemViewSet, basename = 'order_items')

#after creating router, create url patterns
urlpatterns = router.urls +[
    
]



#urlpatterns = [
#     path('category_list/', CategoryViewSet.as_view({'get':'list','post':'create' })), #from views.py 
#     path('category_list/<pk>', CategoryDetailViewSet.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})), 
#     path('food_list/', food_list), #from views.py 
#     # path('food_list/<pk>', food_detail) #from views.py 
    
# ]

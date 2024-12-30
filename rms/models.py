from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() #callin get_user_model () to get the user model from the setting.py file 
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name
    
class Food(models.Model):
    food_name = models.CharField(max_length=50)
    food_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #foreign key= category_id
    def __str__(self):
        return f"{self.food_name} - {self.food_price}"
  
class Table(models.Model):
    table_number = models.IntegerField()
    AVAILABLE =  "Available"
    UN_AVAILABLE =  "Unavailable"
    
    RESERVER = {
            AVAILABLE : "Seat Available",
            UN_AVAILABLE:"Seat Unavailable"
            
        
    }
    is_available = models.CharField(max_length=30, choices=RESERVER, default=UN_AVAILABLE)
    def __str__(self):
        return f"Table no: {self.table_number}"

class Order(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE ) 
    total_price= models.FloatField()
    COMPLETED="Order_Complete"
    PENDING= "Pending"
    PREPARING="Preparing"
    CONFIRM_ORDER= "Confirm_Order"
    CANCEL= "Cancel"
    STATUS_CHOICE = {
        COMPLETED:"Order Completed",
        PENDING:"Pending order",
        PREPARING:"Preparing Order",
        CANCEL:"Order Cancelled",
        CONFIRM_ORDER:"Confirmed Order",
        
    }
    order_status = models.CharField(max_length=30, choices=STATUS_CHOICE, default=PENDING)
    payment_status= models.BooleanField(default=False)
    table = models.ForeignKey(Table, on_delete= models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.user}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.order} - {self.food}"
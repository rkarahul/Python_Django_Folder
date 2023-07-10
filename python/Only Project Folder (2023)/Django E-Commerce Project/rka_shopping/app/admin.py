from django.contrib import admin

# Register your models here.
from .models import(
    Customer,
    Product,
    Cart,
    OrderPlaced
)

@admin.register(Customer)
class CustomerModeladmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class CustomerModeladmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand','category','Product_imgage']


@admin.register(OrderPlaced)
class CustomerModeladmin(admin.ModelAdmin):
    list_display = ['id','ordered_date','status','customer','product','user']

@admin.register(Cart)
class CustomerModeladmin(admin.ModelAdmin):
    list_display = ['id', 'Product', 'user']

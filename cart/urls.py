from django.urls import path
from .views import product_upload_cart


urlpatterns = [
    path('products/upload', product_upload_view, name="product_upload_view"),
    path("products/list",products_list,name="products_list_view"),
    path("products/<int:id>/",product_details,name="product_details_view")

]
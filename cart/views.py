from django.shortcuts import render
from .forms import CartUploadForm
from cart.models import Cart
from django.shortcuts import redirect


# Create your views here.
def product_upload_cart(request):
    if request.method == "POST":
        form =  CartUploadForm(request.POST,request.FILES)
        if form.is_vallid():
            form.save()
        else:
            form = product_upload_cart
            return render(request,'cart_system/cart_upload.html',{'form':form})
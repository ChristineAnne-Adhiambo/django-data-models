from django.shortcuts import render
from .forms import ProductUploadForm
from inventory.models import Product
from django.shortcuts import redirect

def product_upload_view(request):
    if request.method == "POST":
        form = ProductUploadForm(request.POST,request.FILES)
        if form.is_valid():
         form.save()
    else:
        form = ProductUploadForm
    return render(request , 'inventory/product_upload.html' , {'form':form})

# Create your views here.
def products_list(request):
   products = Product.objects.all()
   return render(request,"inventory/productList.html",{'product':products})

def product_details(request, id):
   product_dets = Product.objects.get(id=id)
   return render(request,"inventory/productDetails.html",{'product':product_dets})

def edit_product(request,id): 
    edit_products = Product.objects.get(id=id)
    if request.method =='POST':
        form = ProductUploadForm(request.POST,instance=edit_products)
        if form.is_valid():
            form.save()
            return redirect('product_details,id=id')
        else:
            form = ProductUploadForm(instance=edit_products)
            return render(request,'inventory/edit_product.html',{'form':form})
   
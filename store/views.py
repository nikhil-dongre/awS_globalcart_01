from django.shortcuts import redirect, render,get_object_or_404

from orders.models import OrderProduct
from .models import Product,ReviewRating,ProductGallery
from category.models import Category
from carts.models import Cart,CartItem
from carts.views import _card_id
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from .forms import ReviewForm
from django.contrib import messages,auth
# Create your views here.

def product_store(request,category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True)
        paginator = Paginator(products,1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,2)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {'products': paged_products,
               'product_count': product_count}
    return render(request, 'store/store.html',context)

def serch_products(request):
    print('refs')
    if request.method == 'GET':
        print( request.method)
        products = Product.objects.order_by('-created_date').filter(product_name__contains=request.GET['keyword'])
        for product in products:
            print(product.product_name)
        product_count = products.count()
        context ={
        'products': products,
        'product_count': product_count
    }
        return render(request, 'store/store.html', context)
    

def product_details(request,category_slug,product_slug):
    print('INto product slug')
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_card_id(request),product = single_product).exists()
        
    except Exception as e:
        raise e
    if request.user.is_authenticated:
        try:
            order_product = OrderProduct.objects.filter(user = request.user,product_id =single_product.id).exists()
        except OrderProduct.DoesNotExist:
            order_product = None

    else:
        order_product = None
    reviews = ReviewRating.objects.filter(product_id = single_product.id,status=True)

    product_gallery = ProductGallery.objects.filter(product_id = single_product.id)
    
    context ={
        'single_product': single_product,
        'in_cart': in_cart,
        'order_product': order_product,
        'reviews': reviews,
        'product_gallery':product_gallery

    }
    
    return render(request, 'store/product_details.html',context)

def submit_reviews(request, product_id):
    print("submit review")
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id,product__id=product_id)
            form = ReviewForm(request.POST,instance=reviews)
            form.save()
            messages.success(request,"Thank your revew has been Updated")
            return redirect(url)
        except:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.product_id = product_id
                data.user = request.user
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.save()
                messages.success(request,"Thank You,YOur reveiw is submitted")
                return redirect(url)



    
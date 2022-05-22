from sre_parse import State
from statistics import quantiles
from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
#from platformdirs import user_config_path
from .models import Customer, Cart, Product, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductView(View):
    def get(self, request):
        totalitem = 0
        # topwears = Product.objects.filter(category='TW')
        # bottomweres = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/home.html', {
            # 'topwears': topwears,
            # 'bottomwears': bottomweres,
            'mobiles': mobiles,
            'laptops': laptops,
            'totalitem': totalitem,
        })


# def product_detail(request):
#     return render(request, 'app/productdetail.html')


class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {
            'product': product,
            'item_already_in_cart':item_already_in_cart,
            'totalitem': totalitem
        })

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)

        amount = 0.0
        shipping_amount = 60.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_prie)
                amount += tempamount
                totalamount = amount + shipping_amount

            return render(request, 'app/addtocart.html', {
                'carts': cart,
                'totalamount': totalamount,
                'amount': amount,
                'totalitem': totalitem
            })
        else:
            return render(request, 'app/emptycart.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 60.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_prie)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 60.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_prie)
            amount += tempamount
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) 
        c.delete()
        amount = 0.0
        shipping_amount = 60.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_prie)
            amount += tempamount
        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


def buy_now(request):
    return render(request, 'app/buynow.html')

@login_required
def address(request):
    totalitem = 0
    add = Customer.objects.filter(User=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/address.html', {'add': add, 'totalitem': totalitem, 'active': 'bg-info'})

@login_required
def orders(request):
    totalitem = 0
    op = OrderPlaced.objects.filter(user=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/orders.html', {'order_placed': op, 'totalitem': totalitem})


def mobile(request, data=None):
    totalitem = 0
    if data == None:
        mobile = Product.objects.filter(category='M')
    elif data == 'Xiaomi' or data == 'Oppo' or data == 'Apple' or data == 'Samsung' or data == 'Redmi':
        mobile = Product.objects.filter(category='M').filter(brand=data)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/mobile.html', {'mobile': mobile, 'totalitem': totalitem})


def laptop(request, data=None):
    totalitem = 0
    if data == None:
        laptop = Product.objects.filter(category='L')
    elif data == 'Acer' or data == 'Asus' or data == 'Apple' or data == 'Samsung' or data == 'Msi':
        laptop = Product.objects.filter(category='L').filter(brand=data)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/laptop.html', {'laptop': laptop, 'totalitem': totalitem})


def login(request):
    return render(request, 'app/login.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!!. Registered Succesfully, Please Login Now!!.')
            form.save()
           
        return render(request, 'app/customerregistration.html', {'form': form})

# class PasswordChangeView(View):
#     def passwordchange(request):
#         totalitem = 0
#         if request.user.is_authenticated:
#             totalitem = len(Cart.objects.filter(user=request.user))
#         return render(request, 'app/passwordchange.html', {'totalitem': totalitem})

@login_required
def checkout(request):
    totalitem = 0
    user = request.user
    add = Customer.objects.filter(User=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 60.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_prie)
            amount += tempamount
            totalamount = amount + shipping_amount
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/checkout.html',  {
        'add': add,
         'totalamount': totalamount, 
         'cart_items': cart_items, 
         'totalitem': totalitem
         })


def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer,product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

# def profile(request):
#     return render(request, 'app/profile.html')

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        totalitem = 0
        form = CustomerProfileForm()
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html', {'form': form, 'totalitem': totalitem, 'active': 'bg-info'})

    def post(self, request):
        totalitem = 0
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(User=usr, name=name, locality=locality,
                           city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(
                request, 'Congratulation !! Profile Update Successfully!!')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html', {'form': form, 'totalitem':totalitem, 'active': 'btn-primary'})



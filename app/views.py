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
        # topwears = Product.objects.filter(category='TW')
        # bottomweres = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'app/home.html', {
            # 'topwears': topwears,
            # 'bottomwears': bottomweres,
            'mobiles': mobiles,
            'laptops': laptops,
        })


# def product_detail(request):
#     return render(request, 'app/productdetail.html')


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {
            'product': product,
            'item_already_in_cart':item_already_in_cart})

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
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
                'amount': amount
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
    add = Customer.objects.filter(User=request.user)
    return render(request, 'app/address.html', {'add': add, 'active': 'bg-info'})

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed': op})


def mobile(request, data=None):
    if data == None:
        mobile = Product.objects.filter(category='M')
    elif data == 'Xiaomi' or data == 'Oppo' or data == 'Apple' or data == 'Samsung' or data == 'Redmi':
        mobile = Product.objects.filter(category='M').filter(brand=data)
    return render(request, 'app/mobile.html', {'mobile': mobile})


def laptop(request, data=None):
    if data == None:
        laptop = Product.objects.filter(category='L')
    elif data == 'Acer' or data == 'Asus' or data == 'Apple' or data == 'Samsung' or data == 'Msi':
        laptop = Product.objects.filter(category='L').filter(brand=data)
    return render(request, 'app/laptop.html', {'laptop': laptop})


def login(request):
    return render(request, 'app/login.html')


# def customerregistration(request):
#     return render(request, 'app/customerregistration.html')

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


@login_required
def checkout(request):
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
    return render(request, 'app/checkout.html',  {'add': add, 'totalamount': totalamount, 'cart_items': cart_items})


def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrdetPlaced(user=user, customer=customer,product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

# def profile(request):
#     return render(request, 'app/profile.html')

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'bg-info'})

    def post(self, request):
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
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})



from sre_parse import State
from statistics import quantiles
from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
#from platformdirs import user_config_path
from django.conf import settings
from django.core.mail import send_mail
import uuid
from .models import Customer, Cart, Product, OrderPlaced, Verification, Brand
from .forms import CustomerRegistrationForm, CustomerProfileForm, LoginForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator


class ProductView(View):
    def get(self, request):
        totalitem = 0
        electronicsAssessories = Product.objects.filter(category='ElectronicAccessories')
        # bottomweres = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='Mobile')
        laptops = Product.objects.filter(category='Laptop')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/home.html', {
            'electronicsAssessories': electronicsAssessories,
            # 'bottomwears': bottomweres,
            'mobiles': mobiles,
            'laptops': laptops,
            'electronicsAssessories': electronicsAssessories,
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
            if request.user.is_authenticated:
                totalitem = len(Cart.objects.filter(user=request.user))
                return render(request, 'app/emptycart.html',{'totalitem': totalitem})


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


def mobile(request):
    totalitem = 0
    data = request.GET.get('brand')
    if data == None:
        mobile = Product.objects.filter(category='Mobile')
    else:
        mobile = Product.objects.filter(category='Mobile',brand__name=data)
    brand = Brand.objects.all()

    # elif data == 'Xiaomi' or data == 'Oppo' or data == 'Apple' or data == 'Samsung' or data == 'Redmi':
    #     mobile = Product.objects.filter(category='M').filter(brand=data)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/mobile.html', {'mobile': mobile,'brand':brand ,'totalitem': totalitem})


def laptop(request):
    totalitem = 0
    data = request.GET.get('brand')
    if data == None:
        laptop = Product.objects.filter(category='Laptop')
    else:
        laptop = Product.objects.filter(category='Laptop',brand__name=data)
    brand = Brand.objects.all()
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/laptop.html', {'laptop': laptop, 'brand': brand, 'totalitem': totalitem})

def eAccessories(request):
    totalitem = 0
    data = request.GET.get('brand')
    if data == None:
        eAccessories = Product.objects.filter(category='ElectronicAccessories')
    else:
        eAccessories = Product.objects.filter(category='ElectronicAccessories',brand__name=data)
    brand = Brand.objects.all()
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/eAssessories.html', {'totalitem': totalitem,'brand': brand, 'eAccessories': eAccessories})

class LogInView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'app/login.html',{'form':form})
    def post(self, request):
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            pro = Verification.objects.get(user=user)
            if pro.verify:
                login(request, user)
                return redirect('/profile/')
            else:
                messages.info(request, 'Your account is\'t verified, Please Check Your Email Account.')
                return redirect('/accounts/login/')
        else:
            return render(request, 'app/login.html',{'form':form})



class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            uid = uuid.uuid4()
            pro_obj = Verification(user=new_user, token=uid)
            pro_obj.save()
            send_email_after_registration(new_user.email, uid)
            messages.success(request, "Your Account Created Successful, To Verifi your account Check your email.")
            return render(request, 'app/customerregistration.html', {'form': form})
        return render(request, 'app/customerregistration.html', {'form': form})

def send_email_after_registration(email, token):
    subject = "Verify Email"
    message = f"""
    Dear Sir/Madam,

    ATTN : Please do not reply to this email.This mailbox is not monitored and you will not receive a response.

    Your Verification Email is Given bellow 👇
    Click on the link to verify your account https://lespstore.pythonanywhere.com/account-verify/{token}

    If you have any queries, Please contact us at,

    LegendSpam Store,
    kirtipur,Kathmandu, Nepal.
    Phone # +9779862413503
    Email Id: lespstore02595@gmail.com
    Portfolio: amritgiri01.com.np

    Warm Regards,
    LegendSpam Store

    """
    print("\n\n")
    print(message,"\n")
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

def account_verify(request, token):
	pf = Verification.objects.filter(token=token).first()
	pf.verify = True
	pf.save()
	messages.success(request, "Your Account has been Verified, You can Login Now.")
	return redirect('/accounts/login/')

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
            nptotal = round(totalamount / 132, 2)

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/checkout.html',  {
        'add': add,
         'totalamount': totalamount,
         'cart_items': cart_items,
         'totalitem': totalitem,
         'nptotal': nptotal,
         'amount': amount
         })
    else:
        messages.warning(request, "Please Select your Placed Address.")
        return redirect('/address/')


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
            return redirect('/address/')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html', {'form': form, 'totalitem':totalitem, 'active': 'btn-primary'})



from django.http import Http404
from django.shortcuts import render,redirect
from blog.forms import  RegisterForm,login_form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Product






def regisetr_pg(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
 
         user = form.save(commit=False)
         user.set_password(form.cleaned_data['password'])
         user.save()
         messages.success(request,"Register Successfully")
         return redirect("login")
        
    return render(request, "register.html", {"form": form})
def login_pg(request):
    form = login_form()
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password =form.cleaned_data['password']
            
            user = authenticate(username= username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfully!")
                return redirect("home")
            return render(request,"login.html", {"form": form})

              
               

    return render(request,"login.html")

def home_pg(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})



   

def detail(request, post_id):
    try:
        product = Product.objects.get(pk=post_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    
    # Get existing cart from session
    cart = request.session.get('cart', {})

    # Add product to cart or update quantity
    if str(post_id) in cart:
        cart[str(post_id)] += 1
    else:
        cart[str(post_id)] = 1

    # Save cart back to session
    request.session['cart'] = cart

    messages.success(request, f"'{product.name}' added to cart.")
    return redirect('home')  # redirect back to home page
def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for pk, qty in cart.items():
        try:
            product = Product.objects.get(pk=pk)
            subtotal = product.price * qty
            total += subtotal
            products.append({
                "product": product,
                "qty": qty,
                "subtotal": subtotal
            })
        except Product.DoesNotExist:
            pass

    return render(request, "cart.html", {
        "products": products,
        "total": total
    })
def remove_cart(request, post_id):
    cart = request.session.get('cart', {})
    if str(post_id) in cart:
        del cart[str(post_id)]
        request.session['cart'] = cart
        messages.success(request, "Item removed from cart.")
    return redirect('cart')
def update_cart(request):
    if request.method == "POST":
        cart = request.session.get('cart', {})
        for key, value in request.POST.items():
            if key.startswith("quantity_"):
                product_id = key.split("_")[1]
                qty = int(value)
                if qty > 0:
                    cart[product_id] = qty
                else:
                    cart.pop(product_id, None)
        request.session['cart'] = cart
        messages.success(request, "Cart updated successfully.")
    return redirect('cart')

def place_order(request):
    request.session['cart'] = {}  # clear cart
    messages.success(request, "Order placed successfully!")
    return redirect('home')
    
def logout_fn(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


    


